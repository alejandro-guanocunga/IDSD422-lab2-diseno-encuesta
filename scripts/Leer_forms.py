"""Convierte la exportación de Google Forms al formato de su CSV.
 
Uso (desde la raíz del repositorio):
    python scripts/Leer_forms.py plantillas/respuestas_forms.csv
 
Entrada : CSV descargado de Google Forms (Respuestas > hoja de cálculo > Descargar CSV).
Salidas : plantillas/encuesta_reales.csv        (solo las respuestas reales, ya codificadas)
          plantillas/encuesta_respuestas.csv    (reales + simuladas, si existe encuesta_simulados.csv)
 
Las columnas se buscan por el TEXTO de la pregunta (no por posición), porque
Google Forms exporta en el orden en que se crearon las preguntas, que puede
no coincidir con el orden en que aparecen en el formulario.
Las opciones deben estar escritas exactamente como en el cuestionario.
"""
import re
import sys
import pandas as pd
 
RUTA = sys.argv[1] if len(sys.argv) > 1 else "plantillas/respuestas_forms.csv"
 
COLUMNAS = (
    ["respuesta_id", "origen", "p1_edad", "p2_prob_inscripcion", "p3_frecuencia", "p4_gasto"]
    + ["p5_atencion", "p5_precios", "p5_variedad", "p5_limpieza", "p5_comodidad"]
    + ["p6_abarrotes", "p6_lacteos", "p6_carnicos", "p6_frutas_vegetales",
       "p6_bebidas", "p6_limpieza_aseo", "p6_cuidado_personal", "p6_otro"]
    + ["p7_beneficio", "p7_otro_texto"]
    + ["p8_descuentos", "p8_puntos", "p8_2x1", "p8_cupones",
       "p8_entrega_domicilio", "p8_ofertas_personalizadas"]
)
 
# --- Códigos (iguales a la tabla del cuestionario) ---
P1 = {"18–20": 1, "21–30": 2, "31–40": 3, "41–50": 4, "51–60": 5, "Mayor a 60 años": 6}
P2 = {"Nada probable": 1, "Poco probable": 2, "Neutral": 3, "Probable": 4, "Muy probable": 5}
P3 = {"Ninguna": 0, "1 a 2 veces": 1, "3 a 4 veces": 2, "5 a 6 veces": 3, "Más de 6": 4}
P4 = {"Menos de 100 USD": 1, "100 a 250 USD": 2, "251 a 500 USD": 3,
      "Más de 500 USD": 4, "Prefiero no responder": 5}
P5 = {"Muy insatisfecho": 1, "Insatisfecho": 2, "Ni satisfecho ni insatisfecho": 3,
      "Satisfecho": 4, "Muy satisfecho": 5}
P8 = {"Nada importante": 1, "Poco importante": 2, "Neutral": 3, "Importante": 4,
      "Muy importante": 5}
P6 = {"Abarrotes": "p6_abarrotes", "Lácteos": "p6_lacteos", "Cárnicos": "p6_carnicos",
      "Frutas y vegetales": "p6_frutas_vegetales", "Bebidas": "p6_bebidas",
      "Limpieza y aseo": "p6_limpieza_aseo", "Cuidado personal": "p6_cuidado_personal"}
P7 = {"Descuentos directos": "descuentos_directos", "Acumulación de puntos": "puntos",
      "Productos 2x1": "2x1", "Cupones de regalo": "cupones", "Ninguno": "ninguno"}
 
 
def limpiar(x):
    """Quita espacios y unifica guiones (18-20 / 18—20 -> 18–20)."""
    return str(x).strip().replace("—", "–").replace("-", "–")
 
 
def codificar(serie, mapa, nombre, limpiar_guiones=False):
    base = serie.map(limpiar) if limpiar_guiones else serie.astype(str).str.strip()
    codigos = base.map(mapa)
    if codigos.isna().any():
        malos = sorted(set(base[codigos.isna()]))
        sys.exit(f"ERROR en {nombre}: opciones que no coinciden con el cuestionario: {malos}")
    return codigos.astype(int)
 
 
def norm(t):
    """Minúsculas y espacios/saltos de línea colapsados, para comparar textos."""
    return re.sub(r"\s+", " ", str(t)).strip().lower()
 
 
def col(df, *fragmentos):
    """Devuelve la columna cuyo título contiene TODOS los fragmentos (sin importar mayúsculas)."""
    frags = [norm(f) for f in fragmentos]
    hallazgos = [c for c in df.columns if all(f in norm(c) for f in frags)]
    if len(hallazgos) != 1:
        sys.exit(f"ERROR: se buscaba 1 columna con {list(fragmentos)} y se encontraron "
                 f"{len(hallazgos)}: {hallazgos}")
    return df[hallazgos[0]]
 
 
forms = pd.read_csv(RUTA, encoding="utf-8-sig")
# 'Marca temporal' no se usa en ningún momento (anonimato)
 
out = pd.DataFrame()
out["origen"] = ["real"] * len(forms)
out["p1_edad"] = codificar(col(forms, "rango de edad"), P1, "P1", limpiar_guiones=True)
out["p2_prob_inscripcion"] = codificar(col(forms, "qué tan probable"), P2, "P2")
out["p3_frecuencia"] = codificar(col(forms, "cuántas veces realizó compras"), P3, "P3")
out["p4_gasto"] = codificar(col(forms, "gasto mensual"), P4, "P4")
 
# P5: una columna por aspecto (el texto entre corchetes identifica cada una)
for nombre, aspecto in [("p5_atencion", "[Atención del personal]"),
                        ("p5_precios", "[Precios]"),
                        ("p5_variedad", "[Variedad de productos]"),
                        ("p5_limpieza", "[Limpieza]"),
                        ("p5_comodidad", "[Comodidad]")]:
    out[nombre] = codificar(col(forms, "satisfecho o satisfecha", aspecto), P5, nombre)
 
# P6: casillas de verificación -> una columna 0/1 por opción; lo desconocido cuenta como 'otro'
p6 = col(forms, "tipos de productos")
marcadas = p6.fillna("").astype(str).apply(lambda t: [s.strip() for s in t.split(",") if s.strip()])
for etiqueta, c in P6.items():
    out[c] = marcadas.apply(lambda l, e=etiqueta: int(e in l))
out["p6_otro"] = marcadas.apply(lambda l: int(any(s not in P6 for s in l)))
 
# P7: lo que no es una opción conocida se trata como 'otro' y se guarda el texto
p7 = col(forms, "beneficio valoraría").astype(str).str.strip()
out["p7_beneficio"] = p7.map(P7).fillna("otro")
out["p7_otro_texto"] = p7.where(~p7.isin(P7.keys()), "")
 
# P8: una columna por beneficio
for nombre, beneficio in [("p8_descuentos", "[Descuentos directos]"),
                          ("p8_puntos", "[Acumulación de puntos]"),
                          ("p8_2x1", "[Productos 2x1]"),
                          ("p8_cupones", "[Cupones de regalo"),
                          ("p8_entrega_domicilio", "[Entregas a domicilio]"),
                          ("p8_ofertas_personalizadas", "[Ofertas personalizadas]")]:
    out[nombre] = codificar(col(forms, "qué tan importante es cada uno", beneficio), P8, nombre)
 
# Filtro de población: quien no compró el mes anterior (P3 = 0) queda fuera
fuera = (out["p3_frecuencia"] == 0).sum()
out = out[out["p3_frecuencia"] != 0].reset_index(drop=True)
if fuera:
    print(f"Se excluyeron {fuera} respuesta(s) con P3 = Ninguna (fuera de la población).")
 
out.insert(0, "respuesta_id", [f"R{i:03d}" for i in range(1, len(out) + 1)])
out[COLUMNAS].to_csv("plantillas/encuesta_reales.csv", index=False)
print(f"{len(out)} respuestas reales -> plantillas/encuesta_reales.csv")
 
# Unir con las simuladas (si existen) y renumerar los IDs en secuencia
try:
    sim = pd.read_csv("plantillas/encuesta_simulados.csv")
    todo = pd.concat([out[COLUMNAS], sim[COLUMNAS]], ignore_index=True)
    todo["respuesta_id"] = [f"R{i:03d}" for i in range(1, len(todo) + 1)]
    todo.to_csv("plantillas/encuesta_respuestas.csv", index=False)
    print(f"{len(todo)} filas en total -> plantillas/encuesta_respuestas.csv")
except FileNotFoundError:
    print("No se encontró plantillas/encuesta_simulados.csv; corre generar_simulados.py para unirlas.")
 
