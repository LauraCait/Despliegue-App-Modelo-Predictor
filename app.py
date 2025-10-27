import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# Añadir el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from diccionario import MAPPINGS, get_mapping
from model import DropoutPredictor
from utils import (
    plot_confusion_matrix, 
    plot_feature_importance, 
    plot_metrics_comparison,
    format_prediction_result,
    create_sample_input,
    validate_input_data,
    display_data_info
)

st.set_page_config(page_title="Predictor de Deserción Estudiantil", layout="wide", page_icon=":mortar_board:", initial_sidebar_state="expanded")

st.markdown("""
    <style>
        /* Fondo del sidebar */
        [data-testid="stSidebar"] {
            background-color: #1F305E; /* Azul oscuro */
            color: white;
        }

        /* Color del título del sidebar */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: white;
        }

        /* Color del texto */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
            color: #1F305E;
        }

        /* Color del selectbox (fondo blanco con bordes suaves) */
        [data-testid="stSidebar"] .stSelectbox {
            background-color: white;
            border-radius: 8px;
            padding: 5px;
        }

        /* Opcional: cambiar el color de hover */
        [data-testid="stSidebar"] .stSelectbox:hover {
            background-color: #f9fafb;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("🎓 Predictor de Deserción Estudiantil")
st.markdown("---")

# Inicializar objetos en session_state
if 'model' not in st.session_state:
    st.session_state.model = DropoutPredictor()

if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False

if 'model_trained' not in st.session_state:
    st.session_state.model_trained = False

# Sidebar para navegación
st.sidebar.title("Navegación")
page = st.sidebar.selectbox(
    "Selecciona una página:",
    ["🏠 Inicio", "📊 Datos", "🔮 Predicciones", "📈 Análisis"]
)

# Página de Inicio
if page == "🏠 Inicio":
    st.header("Bienvenido al Predictor de Deserción Estudiantil")
    
    st.markdown("""
    Esta aplicación utiliza Machine Learning para predecir la probabilidad de deserción estudiantil 
    basándose en diversos factores académicos, socioeconómicos y demográficos.
    
    ### 🚀 Características principales:
    - **Carga de datos**: Importa y visualiza datasets de estudiantes
    - **Entrenamiento de modelo**: Utiliza Random Forest optimizado con hiperparámetros ajustados
    - **Predicciones**: Realiza predicciones individuales o en lote
    - **Análisis**: Visualiza métricas de rendimiento y importancia de características
    
    ### 📋 Instrucciones de uso:
    1. **Datos**: Los datos se cargan automáticamente desde la carpeta data/
    2. **Predicciones**: Realiza predicciones individuales o con datos reales (el modelo se entrena automáticamente)
    3. **Análisis**: Explora el rendimiento del modelo y las características más importantes
    
    ### 🎯 Clases de predicción:
    - **Dropout**: Estudiante que abandona los estudios
    - **Enrolled**: Estudiante que continúa matriculado
    - **Graduate**: Estudiante que se gradúa exitosamente
    """)

# Página de Datos
elif page == "📊 Datos":
    st.header("📊 Datos del Proyecto")
    
    # Cargar datos automáticamente al iniciar
    if not st.session_state.data_loaded:
        try:
            data_path = "data/data.csv"
            if os.path.exists(data_path):
                df = pd.read_csv(data_path, sep=";")
                st.session_state.df = df
                st.session_state.data_loaded = True
                st.success("✅ Datos cargados automáticamente")
            else:
                st.error("❌ No se encontró el archivo data/data.csv")
        except Exception as e:
            st.error(f"❌ Error al cargar los datos: {str(e)}")
    
    if st.session_state.data_loaded:
        st.subheader("Exploración de Datos")
        df = st.session_state.df
        
        # Información básica
        display_data_info(df)
        
        # Mostrar primeras filas
        st.subheader("Vista Previa de los Datos")
        st.dataframe(df.head(10))
        
        # Estadísticas descriptivas
        if st.checkbox("Mostrar estadísticas descriptivas"):
            st.subheader("Estadísticas Descriptivas")
            st.dataframe(df.describe())

# Página de Predicciones
elif page == "🔮 Predicciones":
    st.header("🔮 Realizar Predicciones")
    
    # El modelo se entrena automáticamente cuando se necesita
    if True:
        tab1 = st.tabs(["Predicción Individual"])[0]
        
        with tab1:
            st.subheader("Predicción para un Estudiante")
            
            # Crear formulario para entrada de datos
            with st.form("prediction_form"):
                st.write("Ingresa los datos del estudiante:")
                
                # Obtener datos de ejemplo
                sample_data = create_sample_input()
                
                # Crear inputs organizados en columnas
                col1, col2, col3 = st.columns(3)
                input_data = {}
                
                # Dividir las características en grupos
                features = list(sample_data.keys())
                features_per_col = len(features) // 3 + 1
                
                with col1:
                    st.write("**Información Personal**")
                    for feature in features[:features_per_col]:
                        mapping = get_mapping(feature)
                        if mapping:
                            seleccion = st.selectbox(feature, list(mapping.keys()))
                            input_data[feature] = mapping[seleccion]
                        else:
                            # Inputs numéricos
                            if isinstance(sample_data[feature], float):
                                input_data[feature] = st.number_input(
                                    feature, 
                                    value=float(sample_data[feature]),
                                    format="%.2f"
                                )
                            else:
                                input_data[feature] = st.number_input(
                                    feature, 
                                    value=int(sample_data[feature])
                                )
                
                with col2:
                    st.write("**Información Académica**")
                    for feature in features[features_per_col:2*features_per_col]:
                        mapping = get_mapping(feature)
                        if mapping:
                            seleccion = st.selectbox(feature, list(mapping.keys()))
                            input_data[feature] = mapping[seleccion]
                        else:
                            if isinstance(sample_data[feature], float):
                                input_data[feature] = st.number_input(
                                    feature, 
                                    value=float(sample_data[feature]),
                                    format="%.2f"
                                )
                            else:
                                input_data[feature] = st.number_input(
                                    feature, 
                                    value=int(sample_data[feature])
                                )
                
                with col3:
                    st.write("**Información Económica y Familiar**")
                    for feature in features[2*features_per_col:]:
                        mapping = get_mapping(feature)
                        if mapping:
                            seleccion = st.selectbox(feature, list(mapping.keys()))
                            input_data[feature] = mapping[seleccion]
                        else:
                            if isinstance(sample_data[feature], float):
                                input_data[feature] = st.number_input(
                                    feature, 
                                    value=float(sample_data[feature]),
                                    format="%.2f"
                                )
                            else:
                                input_data[feature] = st.number_input(
                                    feature, 
                                    value=int(sample_data[feature])
                                )
                
                submitted = st.form_submit_button("🔮 Realizar Predicción")
                
                if submitted:
                    try:
                        # Realizar predicción
                        prediction, probabilities = st.session_state.model.predict_single(input_data)
                        
                        # Obtener nombres de clases (orden correcto según codificación)
                        class_names = ['Dropout', 'Enrolled', 'Graduate']
                        
                        # Formatear resultado
                        result = format_prediction_result(prediction, probabilities, class_names)
                        
                        # Mostrar resultado
                        st.subheader("📊 Resultado de la Predicción")
                        
                        col_r1, col_r2 = st.columns(2)
                        
                        with col_r1:
                            # Predicción principal
                            if result['prediction'] == 'Dropout':
                                st.error(f"🚨 **Predicción: {result['prediction']}**")
                            elif result['prediction'] == 'Graduate':
                                st.success(f"🎓 **Predicción: {result['prediction']}**")
                            else:
                                st.info(f"📚 **Predicción: {result['prediction']}**")
                            
                            st.write(f"**Confianza: {result['confidence']:.2%}**")
                        
                        with col_r2:
                            st.write("**Probabilidades por clase:**")
                            for class_name, prob in result['probabilities'].items():
                                st.write(f"- {class_name}: {prob:.2%}")
                        
                        # Mostrar probabilidades como texto
                        st.write("**Distribución de probabilidades:**")
                        for class_name, prob in result['probabilities'].items():
                            st.progress(prob, text=f"{class_name}: {prob:.2%}")
                        
                    except Exception as e:
                        st.error(f"❌ Error al realizar la predicción: {str(e)}")

# Página de Análisis
elif page == "📈 Análisis":
    st.header("📈 Análisis del Modelo")
    
    # El modelo se entrena automáticamente cuando se necesita
    if True:
        tab1, tab2, tab3 = st.tabs(["Métricas", "Matriz de Confusión", "Importancia de Características"])
        
        with tab1:
            try:
                # Cargar datos de prueba y evaluar
                X_test = pd.read_csv("data/X_test.csv")
                y_test_df = pd.read_csv("data/y_test.csv")
                y_test = y_test_df.iloc[:, 0].values
                
                metrics, report, cm = st.session_state.model.evaluate(X_test, y_test)
                
                st.subheader("📊 Métricas de Evaluación")
                
                # Mostrar métricas en tarjetas
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Accuracy", f"{metrics['accuracy']:.3f}")
                with col2:
                    st.metric("Precision", f"{metrics['precision']:.3f}")
                with col3:
                    st.metric("Recall", f"{metrics['recall']:.3f}")
                with col4:
                    st.metric("F1-Score", f"{metrics['f1_score']:.3f}")
                
                # Gráfico de métricas
                fig_metrics = plot_metrics_comparison(metrics)
                st.pyplot(fig_metrics)
                
                # Reporte detallado
                if st.checkbox("Mostrar reporte detallado"):
                    st.subheader("📋 Reporte de Clasificación Detallado")
                    
                    report_df = pd.DataFrame(report).transpose()
                    # Convertir tipos para evitar error de Arrow
                    display_report = report_df.copy()
                    for col in display_report.columns:
                        if display_report[col].dtype == 'object':
                            display_report[col] = display_report[col].astype(str)
                    st.dataframe(display_report)
            
            except Exception as e:
                st.error(f"❌ Error al evaluar el modelo: {str(e)}")
        
        with tab2:
            try:
                # Cargar datos de prueba y evaluar
                X_test = pd.read_csv("data/X_test.csv")
                y_test_df = pd.read_csv("data/y_test.csv")
                y_test = y_test_df.iloc[:, 0].values
                
                metrics, report, cm = st.session_state.model.evaluate(X_test, y_test)
                
                st.subheader("🎯 Matriz de Confusión")
                
                class_names = ['Dropout', 'Enrolled', 'Graduate']
                fig_cm = plot_confusion_matrix(cm, class_names)
                st.pyplot(fig_cm)
                
                # Interpretación
                st.subheader("📖 Interpretación")
                st.write("""
                La matriz de confusión muestra cómo el modelo clasifica cada clase:
                - **Diagonal principal**: Predicciones correctas
                - **Fuera de la diagonal**: Errores de clasificación
                - **Filas**: Clases reales
                - **Columnas**: Clases predichas
                """)
            
            except Exception as e:
                st.error(f"❌ Error al generar matriz de confusión: {str(e)}")
        
        with tab3:
            # El modelo se entrena automáticamente
            if True:
                st.subheader("🔍 Importancia de las Características")
                
                # Obtener importancia de características
                try:
                    X_train = pd.read_csv("data/X_train.csv")
                    feature_names = X_train.columns.tolist()
                    feature_importance = st.session_state.model.get_feature_importance(feature_names)
                    
                    # Selector para número de características a mostrar
                    top_n = st.slider("Número de características a mostrar", 5, 30, 15)
                    
                    # Gráfico de importancia
                    fig_importance = plot_feature_importance(feature_importance, top_n)
                    st.pyplot(fig_importance)
                    
                    # Tabla de importancia
                    if st.checkbox("Mostrar tabla de importancia"):
                        st.subheader("📊 Tabla de Importancia")
                        # Convertir tipos para evitar error de Arrow
                        display_importance = feature_importance.head(top_n).copy()
                        for col in display_importance.columns:
                            if display_importance[col].dtype == 'object':
                                display_importance[col] = display_importance[col].astype(str)
                        st.dataframe(display_importance)
                        
                except Exception as e:
                    st.error(f"Error al obtener importancia: {str(e)}")
                
                # Interpretación
                st.subheader("📖 Interpretación")
                st.write("""
                La importancia de las características indica qué variables son más relevantes 
                para el modelo al hacer predicciones:
                - **Valores altos**: Características muy importantes para la predicción
                - **Valores bajos**: Características menos relevantes
                - Las características se ordenan de mayor a menor importancia
                """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>🎓 Predictor de Deserción Estudiantil | Desarrollado con Streamlit y Scikit-learn</p>
    </div>
    <div style='text-align: center'>
        <p>💻 <strong><em>Desarrollado por Laura Valentina Caicedo y Juan José Muñoz</em></strong></p>
    </div>
    """, 
    unsafe_allow_html=True
)