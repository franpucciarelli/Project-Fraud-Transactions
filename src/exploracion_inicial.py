"""
Exploración Inicial de Datos: Data Understanding

En esta etapa voy a hacer lo que en un "entorno real" debería presentarme como documentación.
Me refiero a entender cómo la empresa/entidado recolecta la información: ¿Qué datos se guardan? ¿Están rotos? ¿Faltan campos?
¿De qué tipos son?, etc.
A falta de alguien que me cuente todo esto sobre los datos que vamos a estar trabajando, lo hago a mano por mi cuenta.
En el fondo, busco entender la estructura del negocio.
"""

# %%

import pandas as pd 
from config import RAW_BANK_FRAUD


# %% 

data:pd.DataFrame = pd.read_csv(RAW_BANK_FRAUD)

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
'''
Veamos cómo el DataSet maneja valores Null. 
Es decir ¿Existen filas con 'NaN'? ¿O quien recolecta la información nos asegura que no existen campos que pueden quedar vacíos?
En el fondo, entendamos la consistencia de la información. Importantísimo si luego queremos entrenar modelos.
'''

# Busquemos filas con algún valor 'NaN'.
print(data.isnull().any(axis=1).sum())

'''
Ok... encontramos bastantes registros con información faltante. Más del 90% de hecho.
Con eso voy a tener que tener mucho cuidado al momento de tomar columnas para entrenar modelos. Intentar tomar columnas
que tengan de poca a ningúna información faltante. Para el modelo quede consistente.
'''

'''
Si el DataSet es consistente, no va a tener filas idénticas/repetidas. Supongo que 'transaction_id' funciona como 
clave primaria. Veamoslo por las dudas.
'''
print((data['transaction_id'].nunique()) == (len(data)))
# Bien... tengo la clave primaria identificada, y no tengo dos filas con la misma información.


# %% 

# Pasemos a la columna más importante para el modelo que voy a entrenar: la columna 'is_fraud'.

# Primero observo una columna llamada 'fraud_type' ¿Qué información tiene esta columna?
print(data['fraud_type'].head(15), '\n')

'''
Ok... esta columna explica muchas cosas. Al parecer, todas las transacciones que no son fraudulentas ('is_fraud' = 0) tienen 
'NaN' en 'fraud_type'. 
Analiecmos más en profundidad esta columna.
'''

# ¿Todas las transacciones clasificadas como fraudulentas tienen su tipo de fraude especificado?
print(f"Cantidad de transacciones fraudulentas: {data['is_fraud'].sum()}")
print(f"Cantidad de transacciones con fraude clasificado: {data['fraud_type'].count()}", '\n')
# Ok... pareciera que sí.

# Me interesa saber cuántos tipos de fraude clasifican.
print(f"Cantidad de tipos de fraude clasificados: {len(data['fraud_type'].unique())}")
# Ok... es una cantidad super manejable. A ver cuáles son:
print(f"Tipos de Fraude clasificados: {data['fraud_type'].unique()}", '\n')

# Veamos qué tan desbalanceado está el problema de las transacciones fraudulentas.
print(data['is_fraud'].value_counts(), '\n')
print((data['is_fraud'].value_counts() / len(data)) * 100, '\n')
# Bueno... recontra desbalanceado. Sólo el 5% de las transacciones totales son fraudulentas.

# Fin.