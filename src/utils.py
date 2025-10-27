import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay
import streamlit as st

def plot_confusion_matrix(cm, class_names, title="Matriz de Confusión"):
    """Crear gráfico de matriz de confusión"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
    disp.plot(ax=ax, cmap='viridis')
    
    plt.title(title)
    plt.tight_layout()
    return fig

def plot_feature_importance(feature_importance_df, top_n=15):
    """Crear gráfico de importancia de características"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    top_features = feature_importance_df.head(top_n)
    
    sns.barplot(data=top_features, x='importance', y='feature', ax=ax)
    plt.title(f'Top {top_n} Características Más Importantes')
    plt.xlabel('Importancia')
    plt.ylabel('Características')
    plt.tight_layout()
    
    return fig

def plot_metrics_comparison(metrics_dict):
    """Crear gráfico de comparación de métricas"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    metrics_names = list(metrics_dict.keys())
    metrics_values = list(metrics_dict.values())
    
    bars = ax.bar(metrics_names, metrics_values, color=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
    
    # Añadir valores en las barras
    for bar, value in zip(bars, metrics_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{value:.3f}', ha='center', va='bottom')
    
    plt.title('Métricas de Evaluación del Modelo')
    plt.ylabel('Valor')
    plt.ylim(0, 1.1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig

def format_prediction_result(prediction, probabilities, class_names):
    """Formatear resultado de predicción para mostrar"""
    predicted_class = class_names[prediction]
    
    result = {
        'prediction': predicted_class,
        'confidence': probabilities[prediction],
        'probabilities': {class_names[i]: prob for i, prob in enumerate(probabilities)}
    }
    
    return result

def create_sample_input():
    """Crear datos de ejemplo para pruebas"""
    try:
        X_train = pd.read_csv("data/X_train.csv")
        # Toma la primera fila como base de ejemplo
        sample_data = X_train.iloc[0].to_dict()
    except Exception as e:
        st.error(f"⚠️ No se pudo cargar X_train.csv: {str(e)}")
        # Fallback si falla la carga
        sample_data = {}
        
    return sample_data

def validate_input_data(data, expected_features):
    """Validar que los datos de entrada tengan las características esperadas"""
    missing_features = set(expected_features) - set(data.keys())
    extra_features = set(data.keys()) - set(expected_features)
    
    if missing_features:
        return False, f"Faltan las siguientes características: {missing_features}"
    
    if extra_features:
        return False, f"Características adicionales no esperadas: {extra_features}"
    
    return True, "Datos válidos"

def display_data_info(df):
    """Mostrar información básica del dataset"""
    st.write("### Información del Dataset")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Número de filas", df.shape[0])
    
    with col2:
        st.metric("Número de columnas", df.shape[1])
    
    with col3:
        if 'Target' in df.columns:
            st.metric("Clases únicas", df['Target'].nunique())
    
    # Mostrar distribución de la variable objetivo si existe
    if 'Target' in df.columns:
        st.write("### Distribución de la Variable Objetivo")
        target_counts = df['Target'].value_counts()
        
        # Usar dataframe en lugar de bar_chart para evitar el error
        st.write("**Conteo por clase:**")
        for class_name, count in target_counts.items():
            st.write(f"- {class_name}: {count}")
        
        # Mostrar porcentajes
        target_pct = df['Target'].value_counts(normalize=True) * 100
        st.write("**Porcentajes:**")
        for class_name, pct in target_pct.items():
            st.write(f"- {class_name}: {pct:.2f}%")