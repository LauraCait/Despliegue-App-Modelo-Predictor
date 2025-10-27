import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import pickle
import os

class DropoutPredictor:
    def __init__(self):
        # Parámetros optimizados 
        self.model_params = {
            'n_estimators': 230,
            'max_depth': 30,
            'min_samples_split': 3,
            'min_samples_leaf': 1,
            'max_features': 'sqrt',
            'bootstrap': False,
            'class_weight': {0: 2.0, 1: 1.0, 2: 1.0},
            'ccp_alpha': 0.0,
            'random_state': 42,
            'n_jobs': -1
        }
        self.model = RandomForestClassifier(**self.model_params)

        # Entrenar automáticamente si existen los datos
        try:
            X_train = pd.read_csv("data/X_train.csv")
            y_train_df = pd.read_csv("data/y_train.csv")
            y_train = y_train_df.iloc[:, 0].values
            self.model.fit(X_train, y_train)
            self.is_trained = True
        except Exception as e:
            print(f"Error... No se pudo entrenar automáticamente: {str(e)}")
            self.is_trained = False
        
    def train(self, X_train, y_train):
        #Entrenar el modelo
        try:
            self.model.fit(X_train, y_train)
            self.is_trained = True
            return True
        except Exception as e:
            print(f"Error durante el entrenamiento: {str(e)}")
            return False
    
    def predict(self, X):
        #Realizar predicciones
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado.")
        return self.model.predict(X)
    
    def predict_proba(self, X):
        #Obtener probabilidades de predicción
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado.")
        return self.model.predict_proba(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluar el modelo"""
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado")
        
        y_pred = self.predict(X_test)
        
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='macro'),
            'recall': recall_score(y_test, y_pred, average='macro'),
            'f1_score': f1_score(y_test, y_pred, average='macro')
        }
        
        # Reporte de clasificación
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Matriz de confusión
        cm = confusion_matrix(y_test, y_pred)
        
        return metrics, report, cm
    
    def get_feature_importance(self, feature_names):
        #Obtener importancia de las características
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado")
        
        importance = self.model.feature_importances_
        feature_importance = pd.DataFrame({
            'feature': feature_names, 'importance': importance}
        ).sort_values('importance', ascending=False).reset_index(drop=True)
        
        return feature_importance
    
    def save_model(self, filepath):
        #Guardar el modelo entrenado
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado")
        
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(self.model, f)
            return True
        except Exception as e:
            print(f"Error al guardar el modelo: {str(e)}")
            return False
    
    def load_model(self, filepath):
        """Cargar un modelo previamente entrenado"""
        try:
            if os.path.exists(filepath):
                with open(filepath, 'rb') as f:
                    self.model = pickle.load(f)
                self.is_trained = True
                return True
            else:
                print(f"El archivo {filepath} no existe")
                return False
        except Exception as e:
            print(f"Error al cargar el modelo: {str(e)}")
            return False
    
    def predict_single(self, features):
        #Predecir para una sola instancia
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado.")
        
        # Convertir a DataFrame si es necesario
        if isinstance(features, dict):
            features_df = pd.DataFrame([features])
        elif isinstance(features, list):
            features_df = pd.DataFrame([features])
        else:
            features_df = features
        
        prediction = self.model.predict(features_df)[0]
        probabilities = self.model.predict_proba(features_df)[0]
        
        return prediction, probabilities