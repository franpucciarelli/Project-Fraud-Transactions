"""
Exploración Inicial de Datos.
"""

import pandas as pd 

# %% 

data:pd.DataFrmae = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Repositorios Git - GitHub/Project-Fraud-Transactions/data/raw/bank_fraud.csv")

# Dimensiones del DataSet.
print(f"El DataSet cuenta con {data.shape[0]} filas y {data.shape[1]} columnas.\n")

# %%

# Veamos qué columnas contiene.
print(data.columns, "\n")

# Me interesa saber qué tipo de datos almacena cada columna. 
data_types:pd.DataFrame = data.dtypes
print("Tipos de Datos de cada columna.")
print(data_types, "\n")

# Hay varias columnas, de información binaria, que extrañamente tienen 'int64'. Seguramente clasifican con ceros y unos.
# Lo reviso:
print(data[["is_weekend", "is_night_transaction", "is_international"]].head(10), "\n")
print(data[["failed_attempts", "is_fraud"]].head(10), "\n")

print(f"Valores distintos de 'is_weekend': {data["is_weekend"].nunique()}")
print(f"Valores distintos de 'is_night_transaction': {data["is_night_transaction"].nunique()}")
print(f"Valores distintos de 'is_international': {data["is_international"].nunique()}")
print(f"Valores dintintos de 'failed_attemps': {data["failed_attempts"].nunique()}")
print(f"Valores distintos de 'is_fraud': {data["is_fraud"].nunique()}", "\n")

'''
Ok... como sospechaba. Todas estas columnas, menos 'failed_attempts', utilizan 'int' como indicador binario.
En la columna 'failed_attempts' pareciera que se cuentan la cantidad de veces que una mism atransacción falló antes de 
concretarse.
'''

print(f"Valores distintos (explícitos) de 'failed_attempts: {data["failed_attempts"].unique()}")
print(f"Cantidad de transacciones que tuvieron intentos fallidos: {len(data.query("failed_attempts != 0"))}", "\n")

'''
Forma alternativa de hacer la misma operación anterior:
print(f"Cantidad de transacciones que tuvieron intentos fallidos: {(data["failed_attempts"] != 0).sum()}")
'''

# %%

# Continuará...

# Fin.