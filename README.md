# Detección de Transacciones Fraudulentas

## DataSet e Información

**DataSet** a trabajar -> [Bank Transaction Fraud Detection Dataset](https://www.kaggle.com/datasets/nafiulislam490/bank-transaction-fraud-detection-dataset/data)

DataSet que simula alrededor de 1.000.000 de transacciones financieras globales reales (a través de 10 países).
Diseñada para detección de transacciones fraudulentas y análisis de riesgo financiero.

**DataSet Overview**
- 1.000.000 filas
- 26 columnas
- Ratio de Fraude: ~5.5% (clasificación realista inbalanceada)
- Período de Tiempo: 2020 - 2024

## Configuración de Python 

Trabajamos el proyecto con Python, bajo una configuración de Anaconda Environments.

**Librerías de Python utilizadas**: 
- pandas
- numpy
- psycopg2-binary
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn

## Hoja de Ruta 

**Etapa 1: Exploración Inicial del DataSet**
- Trabajos iniciales con `pandas` para exploración del DataSet.
- Entendimiento de la información que se almacena, cómo se almacena y el estado de la misma.
- Cosas como entender qué almacena cada columna, tipos de datos, robustez del datasets, balanceo, etc.
- Escritura de un breve y conciso reporte de estado, donde se detalla todo lo descubierto sobre los datos crudos.

**Etapa 2: Configuración de una Base de Datos**
- En Docker, configuración y despliegue de una Base de Datos PostgreSQL.
- Ingesta de Datos: creación de un script que tome el DataSet en `csv` y lo inyecte en la base de datos.

**Etapa 3: ...**

(Under construction...) 