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

- **Tamaño y justificación:** Se empleará una muestra total de 80 filas: 20 respuestas reales (10 por integrante) y 60 respuestas simuladas con código, dentro del rango exigido de 60 a 100 filas. Las respuestas simuladas se usan solo para tener volumen en los ejercicios; se identifican en la columna origen (real / simulado) y los datos reales se analizan por separado.

- **Cómo se seleccionarán los participantes:** Se seleccionará a familiares, amigos y compañeros de universidad que compran habitualmente en las sucursales de RetailAndina en Quito, enviándoles el formulario digital por WhatsApp y correo.

- **Equivalente en código (Python o R):** 
Aunque aplicamos conveniencia por accesibilidad a la red de contactos, el equivalente técnico para simular una extracción reproducible sobre una base de datos de respaldo utiliza una semilla fija:
```

python
import pandas as pd
# Simulación de extracción de respaldo con semilla reproducible
clientes_base = pd.DataFrame({"cliente_id": range(1, 500)})
muestra_aleatoria = clientes_base.sample(n=20, random_state=42)
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
|Sesgo de selección por conveniencia: Al recolectar datos en la red cercana (amigos y familiares), se subrepresenta a clientes mayores o de otros segmentos que compran habitualmente en RetailAndina. | Declarar el canal en la metodología y diversificar el envío del formulario a distintos rangos de edad. Las filas simuladas no corrigen este sesgo: se declaran en la columna origen y los resultados reales se analizan por separado.|
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

Tras ejecutar el script de auditoría (`verificacion_encuesta.py`) sobre el archivo de respuestas integradas (`encuesta_respuestas.csv`), se obtuvieron los siguientes resultados clave para garantizar la integridad de los datos:

- **Tipos de datos (dtypes):** Todas las columnas numéricas y escalas Likert se cargaron correctamente como enteros (`int64`), mientras que los campos descriptivos operan bajo los tipos esperados, sin corromperse durante la lectura del CSV.
- **Valores faltantes (NA):** No se detectaron valores nulos indeseados en las columnas principales, y los campos opcionales manejan adecuadamente los vacíos mediante marcas neutras.
- **Distribuciones y sesgos interpretados:**
  - *Sesgo de selección:* Al basarse en la red de contactos directos, se observa una concentración de respuestas en los rangos de edad más jóvenes (21–30 años), lo que subrepresenta parcialmente a los clientes mayores de RetailAndina.
  - *Sesgo de respuesta:* Las escalas de satisfacción (P5) muestran una tendencia hacia calificaciones altas (positivas), reflejando una leve deseabilidad social típica de encuestas aplicadas a conocidos, aspecto que se mitiga analizando los datos reales de forma independiente a los simulados.


