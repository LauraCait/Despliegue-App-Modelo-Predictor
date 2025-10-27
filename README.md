Predictor de Deserción Estudiantil

Una aplicación web desarrollada con Streamlit que utiliza Machine Learning para predecir la probabilidad de deserción estudiantil basándose en diversos factores académicos, socioeconómicos y demográficos.

Características
- Entrenamiento de modelo: Utiliza Random Forest optimizado con hiperparámetros ajustados
- Predicciones: Realiza predicciones individuales
- Análisis: Visualiza métricas de rendimiento y importancia de características
- Interfaz intuitiva: Navegación fácil con múltiples páginas organizadas

Clases de Predicción

- Dropout: Estudiante que abandona los estudios
- Enrolled: Estudiante que continúa matriculado  
- Graduate: Estudiante que se gradúa exitosamente

Requisitos

- Python 3.8 o superior
- Las dependencias listadas en requirements.txt

Instalación

1. Clona o descarga este repositorio
2. Navega al directorio del proyecto:
3. Instala las dependencias: pip install -r requirements.txt

Ejecución
Para ejecutar la aplicación: streamlit run app.py
La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

Estructura del Proyecto
Despliegue_App_Deserción/
├── app.py                 # Aplicación principal de Streamlit
├── src/
│   ├── data_processing.py # Módulo de procesamiento de datos
│   ├── model.py          # Módulo del modelo de ML
│   └── utils.py          # Utilidades y funciones de visualización
├── data/
│   ├── data.csv          # Dataset principal
│   ├── X_train.csv       # Datos de entrenamiento (características)
│   ├── X_test.csv        # Datos de prueba (características)
│   ├── y_train.csv       # Datos de entrenamiento (etiquetas)
│   └── y_test.csv        # Datos de prueba (etiquetas)
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo

Uso de la Aplicación

1. Página de Inicio
- Información general sobre la aplicación
- Especificaciones del modelo

2. Detalles del dataset
- Visualización, reporte y análisis de los datos

3. Página de Predicciones
- Predicción Individual: Ingresa datos de un estudiante específico

4. Página de Análisis
- Métricas: Visualiza accuracy, precision, recall y F1-score

Especificaciones del Modelo

Algoritmo: Random Forest Classifier

Hiperparámetros optimizados:
- n_estimators: 230
- max_depth: 30
- min_samples_split: 3
- min_samples_leaf: 1
- max_features: 'sqrt'
- bootstrap: False
- class_weight: {0: 2.0, 1: 1.0, 2: 1.0}
- ccp_alpha: 0.0


Formato de Datos

El dataset debe contener las siguientes características:

Información Personal
- Marital status
- Age at enrollment
- Gender
- Nacionality
- Displaced
- Educational special needs
- Debtor
- Scholarship holder
- International

Información Académica
- Application mode
- Application order
- Course
- Daytime/evening attendance
- Previous qualification
- Previous qualification (grade)
- Mother's qualification
- Father's qualification
- Tuition fees up to date
- Curricular units 1st sem (credited, enrolled, evaluations, approved, grade, without evaluations)
- Curricular units 2nd sem (credited, enrolled, evaluations, approved, grade, without evaluations)

Información Económica
- Unemployment rate
- Inflation rate
- GDP

Variable Objetivo (para entrenamiento)
- Target: 'Dropout', 'Enrolled', 'Graduate'


Autores
- Laura Valentina Caicedo
- Juan José Muñoz
