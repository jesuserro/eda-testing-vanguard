# Vanguard A/B Test Analysis

## 📌 Introducción
Bienvenido al **proyecto del Módulo 2**. En este proyecto, aplicarás todos los conocimientos adquiridos hasta ahora y aprenderás nuevas habilidades en las próximas dos semanas. No es necesario que domines todos los conceptos desde el inicio, sino que los irás incorporando progresivamente.

### 📚 Temas que abordarás:
- Análisis exploratorio de datos (EDA) y limpieza de datos
- Métricas de rendimiento
- Pruebas de hipótesis
- Evaluación de experimentos
- Visualización de datos con **Tableau**

## 🏗️ Configuración del Proyecto
- Trabajarás en parejas.
- Se recomienda crear un **tablero Kanban** para gestionar tareas y asignar responsabilidades.

## 📅 Flujo de Trabajo Diario
- Trabajarás por las tardes con tu compañero/a en el proyecto.
- Los dos últimos días del proyecto estarán completamente dedicados a finalizarlo antes de la **presentación final (viernes, semana 6).**

---

## 📜 Enunciado del Proyecto

### 🎯 Contexto
Eres un **analista de datos** en el equipo de Experiencia del Cliente (CX) en **Vanguard**, una empresa de gestión de inversiones en EE.UU. Tu primera tarea es analizar un experimento digital reciente.

### 🔍 El Desafío Digital
Vanguard rediseñó su interfaz de usuario (UI) con el objetivo de mejorar la experiencia online de sus clientes. Se introdujeron **mensajes contextuales y ayudas visuales** con la esperanza de que estos cambios aumentaran la tasa de finalización de procesos en la web.

**Pregunta clave**: ¿El nuevo diseño llevó a una mayor tasa de finalización del proceso?

### ⚡ El Experimento
- Se realizó un **test A/B** del **15/03/2017 al 20/06/2017**.
- **Grupo de Control**: Usó la interfaz tradicional de Vanguard.
- **Grupo de Prueba**: Experimentó con la nueva interfaz digital.
- Ambos grupos atravesaron el mismo flujo de interacción: una página inicial, tres pasos intermedios y una página de confirmación.

**Objetivo**: Evaluar si el nuevo diseño mejora la experiencia del usuario y la tasa de finalización.

---

## 📊 Conjunto de Datos
Trabajarás con tres conjuntos de datos:

1. **Perfiles de Clientes (`df_final_demo`)**  
   - Edad, género y detalles de cuenta de los clientes.

2. **Interacciones Digitales (`df_final_web_data`)**  
   - Datos de navegación y comportamiento del usuario en la web.  
   - Este dataset está dividido en `pt_1` y `pt_2`, por lo que se recomienda fusionarlos antes del análisis.

3. **Participantes del Experimento (`df_final_experiment_clients`)**  
   - Identifica qué clientes formaron parte del test A/B.

### 🛠️ Variables Clave
| Variable              | Descripción |
|----------------------|------------|
| `client_id`         | ID único de cada cliente |
| `variation`         | Indica si el cliente participó en el experimento |
| `visitor_id`        | ID único para cada cliente-dispositivo |
| `visit_id`          | ID único por sesión de visita |
| `process_step`      | Fase del proceso digital en la web |
| `date_time`        | Marca de tiempo de cada interacción |
| `clnt_tenure_yr`   | Antigüedad del cliente en años |
| `clnt_tenure_mnth` | Antigüedad del cliente en meses |
| `clnt_age`         | Edad del cliente |
| `gendr`            | Género del cliente |
| `num_accts`        | Número de cuentas que tiene el cliente |
| `bal`              | Balance total del cliente en todas sus cuentas |
| `calls_6_mnth`     | Llamadas al servicio de atención en los últimos 6 meses |
| `logons_6_mnth`    | Número de veces que inició sesión en 6 meses |

---

## 📅 Plan de Trabajo por Días

### 📌 Semana 5
#### **Día 1 & 2: EDA & Limpieza de Datos**
- Exploración inicial de los datasets.
- Análisis del comportamiento del cliente.

#### **Día 3: Métricas de Rendimiento**
- Definir indicadores de éxito (**KPIs**).
- Comparar el desempeño del grupo de control vs. grupo de prueba.

#### **Día 4 & 5: Pruebas de Hipótesis y Evaluación del Experimento**
- Realizar **pruebas de hipótesis** sobre:
  - **Tasa de finalización**
  - **Tasa de finalización con umbral de costo-efectividad**
  - **Otras hipótesis relevantes**
- Evaluación del diseño del experimento:
  - **Efectividad del diseño**
  - **Duración**
  - **Datos adicionales necesarios**

### 📌 Semana 6
#### **Día 1 & 2: Visualización en Tableau**
- Creación de dashboards interactivos en **Tableau**.

#### **Día 3 & 4: Optimización y Presentación**
- Refinar el análisis y los resultados.
- Preparar la **presentación final**.

---

## 📦 Entregables
### ✅ Requisitos del Proyecto
Para completar el proyecto, debes entregar lo siguiente:

1. Un repositorio en **GitHub** llamado `vanguard-ab-test`.
2. Código funcional en **Jupyter Notebook** y **archivos `.py`** con funciones bien estructuradas.
3. Archivos adicionales como:
   - Dashboard de Tableau.
   - README con la documentación del proyecto.
4. URL de las **diapositivas de la presentación**.
5. **Tablero Kanban** (ej. Trello) con el seguimiento del proyecto.

---

## 🎤 Presentación Final
Presentarás los resultados del proyecto en una reunión de **10 minutos** con la directiva de Vanguard. La presentación debe incluir:

### 🔹 Estructura sugerida:
1. **Título & Equipo** (1 diapositiva)  
2. **Introducción** (1 diapositiva)  
   - Contexto del experimento.
   - Pregunta clave: ¿El nuevo UI mejora la tasa de finalización?
3. **Datos utilizados** (1-2 diapositivas)  
   - Descripción de los datasets y limpieza de datos.
4. **Análisis Exploratorio** (2-3 diapositivas)  
   - Perfil de los clientes y análisis preliminar.
5. **Métricas de Rendimiento** (2-3 diapositivas)  
   - Comparación entre **Grupo Control vs. Grupo Prueba**.
6. **Pruebas de Hipótesis** (2-3 diapositivas)  
   - Resultados estadísticos y su interpretación.
7. **Evaluación del Experimento** (1-2 diapositivas)  
   - Diseño, duración y mejoras sugeridas.
8. **Tableau: Visualizaciones** (2-3 diapositivas)  
   - Dashboards clave e insights relevantes.
9. **Trabajo en equipo y Gestión del Proyecto** (1 diapositiva)  
10. **Desafíos y Aprendizajes** (1-2 diapositivas)  
11. **Conclusiones y Recomendaciones** (1-2 diapositivas)  

### 🚀 Requisitos para la Presentación:
- Las diapositivas deben estar en **Google Slides, Slides.com o Prezi**.
- No se aceptan archivos de PowerPoint o Keynote.

---

## 🎯 Bonus: Tareas Opcionales
Si finalizas todas las tareas principales, puedes explorar:
- **Análisis avanzado del comportamiento del cliente**.
- **Cálculo del tamaño del efecto y potencia estadística**.
- **Desarrollo de una aplicación en Streamlit**.

---

## 🏆 Evaluación del Proyecto
Tu trabajo será evaluado según la rúbrica disponible en el **Student Portal**. Si tienes dudas, consulta con tu instructor.

---

## 📝 Conclusión
Este proyecto es una oportunidad para aplicar habilidades en análisis de datos, pruebas de hipótesis y visualización, al mismo tiempo que trabajas en equipo para resolver un problema del mundo real. 🚀

¡Buena suerte con el análisis del test A/B de Vanguard!
