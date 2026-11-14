import os
import pandas as pd

RUTA = "plantillas/encuesta_respuestas.csv"
if not os.path.exists(RUTA):
    print(f"AVISO: No se encontró {RUTA}. Se usará plantillas/encuesta_simulados.csv para la prueba.")
    RUTA = "plantillas/encuesta_simulados.csv"

df = pd.read_csv(RUTA)

print("=" * 60)
print("AUDITORÍA DE LA ENCUESTA")
print("=" * 60)

print("\n1. Tipos de datos (dtypes):")
print(df.dtypes)

print("\n2. Conteo de datos faltantes (NA) por columna:")
print(df.isna().sum())

print("\n3. Distribución de columnas clave:")
columnas_clave = ["p1_edad", "p3_frecuencia", "p5_atencion", "p7_beneficio", "p8_descuentos"]
for col in columnas_clave:
    if col in df.columns:
        print(f"\n--- {col} ---")
        print(df[col].value_counts(dropna=False).sort_index())
    else:
        print(f"\n--- {col} no encontrada ---")

print("\n4. Distribución por origen (real / simulada):")
print(df["origen"].value_counts())

print("\n5. Distribución en datos reales (origen == 'real'):")
reales = df[df["origen"] == "real"]
if len(reales) == 0:
    print("No hay datos reales aún.")
else:
    for col in ["p1_edad", "p3_frecuencia", "p5_atencion", "p7_beneficio"]:
        if col in reales.columns:
            print(f"\n--- {col} (reales) ---")
            print(reales[col].value_counts(dropna=False).sort_index())

print("\n6. Interpretación de patrones de sesgo:")
print("""
- Sesgo de selección: si en los datos reales la distribución de p1_edad se concentra en uno o dos rangos (p. ej., solo 21–30) o p3_frecuencia solo tiene valores altos, la muestra no representa a todos los clientes habituales. La conveniencia por contactos tiende a sobrerrepresentar jóvenes y personas cercanas a los analistas.
- Sesgo de no respuesta: muchos NA en p4_gasto o respuestas "Prefiero no responder" indican que el gasto es sensible. También la ausencia de respuestas en p7_otro_texto sugiere que la opción "Otro" no se está usando o que hay no respuesta.
- Sesgo de respuesta: si p5_atencion (y otras escalas Likert) tiene casi todos valores 4 o 5, hay poca variabilidad; puede ser aquiescencia (decir lo que se espera) o deseabilidad social. Si p7_beneficio se concentra en una sola opción sin variedad, revisar el diseño de la pregunta.
""")
