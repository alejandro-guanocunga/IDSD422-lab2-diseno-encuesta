# Plantilla de diseño — Encuesta de satisfacción (hito 1)

**Equipo:** 7 · **Integrantes:** Jeriel López, Alejandro-Guanocunga  · <br>**Fecha:** 28/10/2026 <br>
**Repositorio (fork):** github.com/alejandro-guanocunga/IDSD422-lab3-diseno-encuesta
<br>**Enfoque del equipo (aprobado en clase):** Programa de fidelización: satisfacción y beneficios valorados

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

> **Formato del entregable:** exporta esta plantilla completada a PDF, con el enlace de tu fork en la carátula, y guarda el PDF en `informes/` del fork. Entrega el PDF y el enlace del fork en el aula virtual.

## 1. Objetivos de la encuesta

### Objetivo Principal:
Identificar qué beneficios y qué aspectos del servicio valoran más los clientes habituales de RetailAndina en Quito, para orientar el diseño de su programa de fidelización.

### Objetivo Secundario:
Determinar qué porcentaje de clientes actuales estaría dispuesto a inscribirse en el programa de fidelización y cuantificar qué combinación de beneficios priorizan para enfocar las estrategias de retención posteriores de la empresa.

## 2. Población objetivo

- Población: Personas de 18 años o más que realizan compras habituales de consumo en las tiendas y supermercados de RetailAndina S.A. En la ciudad de Quito al menos una vez al mes.

- Límites y justificación: Se restringe geográficamente a la ciudad de Quito urbano y a clientes mayores de edad con una frecuencia de compra mensual mínima, garantizando una población alcanzable para la recolección ágil de respuestas reales entre la red de contactos directos de los integrantes, asegurando además que conozcan la propuesta de valor de la cadena.


## 3. Método de muestreo

- **Método:** Muestreo por conveniencia declarada con referidos (contactos directos que cumplen el perfil de cliente en RetailAndina S.A.).

- **Tamaño y justificación:** Se empleará una muestra total de 94 filas: 34 respuestas reales (tras excluir 1 respuesta con compra nula en el mes anterior) y 60 respuestas simuladas con código, dentro del rango exigido de 60 a 100 filas.

- **Cómo se seleccionarán los participantes:** Se seleccionará a familiares, amigos y compañeros de universidad que compran habitualmente en las sucursales de RetailAndina en Quito, enviándoles el formulario digital por WhatsApp y correo.

- **Equivalente en código (Python o R):** 
Aunque aplicamos conveniencia por accesibilidad a la red de contactos, el equivalente técnico para simular una extracción reproducible sobre una base de datos de respaldo utiliza una semilla fija:

```
python
import pandas as pd
# Simulación de extracción de respaldo con semilla reproducible
clientes_base = pd.DataFrame({"cliente_id": range(1, 500)})
muestra_aleatoria = clientes_base.sample(n=34, random_state=42)
print(muestra_aleatoria.head())
```





## 4. Cuestionario 



| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|----------|------------------|-----------------|-------------------|
| 1 | ¿En qué rango de edad se encuentra? | Categórica ordinal | int64 | 1) 18–20<br>2) 21–30<br>3) 31–40<br>4) 41–50<br>5) 51–60<br>6) Mayor a 60 años |
| 2 | ¿Qué tan probable es que se inscriba en un programa de fidelización de RetailAndina? | Categórica ordinal (escala Likert) | int64 | 1) Nada probable<br>2) Poco probable<br>3) Neutral<br>4) Probable<br>5) Muy probable |
| 3 | Durante el mes anterior, ¿cuántas veces realizó compras en un supermercado? | Categórica ordinal | int64 | 0) Ninguna<br>1) 1 a 2 veces<br>2) 3 a 4 veces<br>3) 5 a 6 veces<br>4) Más de 6 |
| 4 | ¿En qué rango se ubica su gasto mensual aproximado en compras de supermercado? | Categórica ordinal | int64 | 1) Menos de 100 USD<br>2) 100 a 250 USD<br>3) 251 a 500 USD<br>4) Más de 500 USD<br>5) Prefiero no responder |
| 5 | ¿Qué tan satisfecho o satisfecha está con los siguientes aspectos de RetailAndina? (atención del personal, precios, variedad de productos, limpieza y comodidad) | Categórica ordinal (escala Likert) | int64 (una columna por aspecto) | 1) Muy insatisfecho<br>2) Insatisfecho<br>3) Ni satisfecho ni insatisfecho<br>4) Satisfecho<br>5) Muy satisfecho |
| 6 | ¿Qué tipos de productos compra con más frecuencia? Puede marcar más de uno. | Categórica nominal (selección múltiple) | int64 0/1 (una columna por opción) | Abarrotes<br>Lácteos<br>Cárnicos<br>Frutas y vegetales<br>Bebidas<br>Limpieza y aseo<br>Cuidado personal<br>Otro |
| 7 | ¿Qué tipo de beneficio valoraría más en un supermercado? | Categórica nominal | object / str | 1) Descuentos directos<br>2) Acumulación de puntos<br>3) Productos 2x1<br>4) Cupones de regalo<br>5) Otro (especifique)<br>6) Ninguno |
| 8 | ¿Qué tan importante es cada uno de estos beneficios para usted? (descuentos directos, acumulación de puntos, productos 2x1, cupones de regalo, entregas a domicilio, ofertas personalizadas) | Categórica ordinal (escala Likert) | int64 (una columna por beneficio) | 1) Nada importante<br>2) Poco importante<br>3) Neutral<br>4) Importante<br>5) Muy importante |



## 5. Análisis de sesgos

| Sesgo potencial | Mitigación |
|---|---|
|Sesgo de selección por conveniencia: Al recolectar datos en la red cercana (amigos y familiares), se subrepresenta a clientes mayores o de otros segmentos que compran habitualmente en RetailAndina.|
| Sesgo de respuesta: Los encuestados podrían responder lo que consideran socialmente aceptable en lugar de expresar sus preferencias reales. | Garantizar el anonimato de las respuestas y utilizar preguntas neutrales que no sugieran una respuesta deseada. |

## 6. Confidencialidad (RA3)

- **Datos personales que se piden y por qué:**
Se solicita únicamente un dato demográfico: el **rango de edad**. Este dato es necesario para realizar cruces de variables que den sentido al análisis: determinar si algún grupo etario en específico prefiere un tipo de beneficio en particular (descuentos directos, puntos, 2x1 o cupones) o se concentra en ciertos hábitos de gasto. Esta información permite segmentar los resultados y orientar el diseño del programa de fidelización de RetailAndina. No se solicitan nombres, correos, teléfonos, cédulas ni direcciones, y la edad se recopila exclusivamente por rangos para minimizar cualquier riesgo de identificación individual.

- **Plan de anonimización (qué se quita o codifica antes de compartir):**
  - El formulario no recoge datos de identificación directa (nombre, correo, teléfono, cédula). Si los canales digitales (WhatsApp o correo) dejan algún metadato de contacto, este se descarta de inmediato.
  - A cada respuesta procesada se le asigna un ID numérico secuencial (`R001`, `R002`, …) desvinculado por completo de la identidad del encuestado.
  - Las variables categóricas y ordinales se codifican numéricamente según la tabla del cuestionario.
  - La lista de contactos utilizada para la difusión de la encuesta se mantiene estrictamente privada y fuera del repositorio del proyecto.
  - Únicamente se comparte el dataset anonimizado (combinando las respuestas reales y simuladas con su respectiva columna `origen`) y se reportan exclusivamente resultados estadísticos agregados.


## 7. Verificación con herramientas (Python / R)

Tras ejecutar el script de auditoría (`verificacion_encuesta.py`) sobre el archivo integrado (`plantillas/encuesta_respuestas.csv`), que consolida **94 filas en total** (**34 respuestas reales** con `origen == 'real'` y **60 respuestas simuladas** con `origen == 'simulada'`, luego de excluir 1 respuesta del formulario que marcó `"Ninguna"` compra en el mes anterior), se obtuvieron los siguientes resultados:

- **Tipos de datos (dtypes):** Todas las variables numéricas y escalas Likert (`p1_edad`, `p2_prob_inscripcion`, `p3_frecuencia`, `p4_gasto`, variables `p5_*`, `p6_*` y `p8_*`) se cargaron como enteros (`int64`). Las columnas de identificación y texto (`respuesta_id`, `origen`, `p7_beneficio`) se cargaron como `object`, mientras que `p7_otro_texto` se interpretó como `float64` al estar completamente vacía.
- **Valores faltantes (NA):** No se registraron valores faltantes en ninguna de las preguntas obligatorias del cuestionario. Únicamente `p7_otro_texto` presenta 94 valores nulos (`NaN`) debido a que ningún encuestado seleccionó la opción `"Otro"` en P7.
- **Distribuciones y sesgos interpretados (analizados exclusivamente sobre las 34 filas reales):**
  - *Sesgo de selección:* Aunque se aplicó muestreo por conveniencia en la red de contactos, la muestra real logró abarcar varios tramos adultos: 13 encuestados tienen entre 31–40 años, 7 entre 21–30, 7 entre 41–50, 5 entre 18–20 y 2 entre 51–60 años, quedando únicamente sin representación el grupo mayor de 60 años. Las 60 filas simuladas se mantienen identificadas en `origen` y no se usan para corregir este sesgo.
  - *Sesgo de no respuesta:* En gasto mensual (`p4_gasto`), solo 2 de los 34 encuestados reales eligieron `"Prefiero no responder"`, mientras que el resto se concentró en menos de 100 USD (10 personas) y 100 a 250 USD (12 personas), mostrando baja evasión en preguntas económicas.
  - *Sesgo de respuesta:* No se evidencia sesgo de aquiescencia o deseabilidad social positiva; por el contrario, las calificaciones de satisfacción muestran dispersión y opiniones críticas (por ejemplo, en atención del personal `p5_atencion` hubo 8 respuestas en nivel 1 y 4 en nivel 2, frente a 10 en niveles 4 y 5), y en `p7_beneficio` predomina la preferencia por descuentos directos (20) y productos 2x1 (10).

