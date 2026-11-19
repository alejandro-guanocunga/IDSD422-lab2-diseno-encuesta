# verificacion_encuesta.R
ruta <- "plantillas/encuesta_respuestas.csv"
if (!file.exists(ruta)) {
  cat("AVISO: No se encontró", ruta, ". Se usará plantillas/encuesta_simulados.csv para la prueba.\n")
  ruta <- "plantillas/encuesta_simulados.csv"
}
df <- read.csv(ruta, stringsAsFactors = FALSE)

cat("=== Tipos de datos (str) ===\n")
str(df)

cat("\n=== Conteo de datos faltantes (NA) por columna ===\n")
print(colSums(is.na(df)))

cat("\n=== Distribución de columnas clave ===\n")
for (col in c("p1_edad", "p3_frecuencia", "p5_atencion", "p7_beneficio", "p8_descuentos")) {
  if (col %in% names(df)) {
    cat("\n---", col, "---\n")
    print(table(df[[col]], useNA = "ifany"))
  } else {
    cat("\n---", col, "no encontrada ---\n")
  }
}

cat("\n=== Distribución por origen ===\n")
print(table(df$origen))

cat("\n=== Distribución en datos reales ===\n")
reales <- df[df$origen == "real", ]
if (nrow(reales) == 0) {
  cat("No hay datos reales aún.\n")
} else {
  for (col in c("p1_edad", "p3_frecuencia", "p5_atencion", "p7_beneficio")) {
    if (col %in% names(reales)) {
      cat("\n---", col, "(reales) ---\n")
      print(table(reales[[col]], useNA = "ifany"))
    }
  }
}

cat("\n=== Interpretación de patrones de sesgo ===\n")
cat("- Sesgo de selección: revisar concentración de edad y frecuencia.\n")
cat("- Sesgo de no respuesta: revisar NA en gasto y 'Prefiero no responder'.\n")
cat("- Sesgo de respuesta: revisar falta de variabilidad en escalas Likert.\n")
