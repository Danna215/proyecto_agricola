# 🌱 Proyecto: Análisis Exploratorio de Cultivos con Streamlit y Google Colab

Este proyecto corresponde a la **Tarea 1** de la asignatura, enfocado en el **Análisis Exploratorio de Datos (EDA)** para Ingeniería Agrícola.  
Se desarrolla en **dos partes complementarias**:  
1. Un **notebook en Google Colab** con el EDA detallado paso a paso.  
2. Una **aplicación web interactiva en Streamlit** que permite explorar los datos de manera profesional.

---

## 📊 Dataset

- **Nombre:** Crop Recommendation Dataset  
- **Fuente:** [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)  
- **Descripción:** Contiene 2200 registros con información sobre condiciones de suelo y clima para 22 tipos de cultivos.  
- **Variables principales:**  
  - `N`: Nitrógeno  
  - `P`: Fósforo  
  - `K`: Potasio  
  - `temperature`: Temperatura (°C)  
  - `humidity`: Humedad (%)  
  - `ph`: Acidez del suelo  
  - `rainfall`: Lluvia (mm)  
  - `label`: Cultivo recomendado  

---

## 📂 Archivos del Proyecto

- `EDA_colab.ipynb`: Notebook con el análisis exploratorio en Google Colab.  
- `app.py`: Aplicación web interactiva desarrollada en **Streamlit**.  
- `Crop_recommendation.csv`: Dataset base usado en el análisis.  
- `requirements.txt`: Dependencias del proyecto.  
- `README.md`: Este documento de guía y documentación.  

---

## ⚙️ Instalación y Ejecución Local de la App

1. Clonar este repositorio o descargarlo como ZIP.  
2. Crear y activar un entorno virtual (recomendado):  

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
