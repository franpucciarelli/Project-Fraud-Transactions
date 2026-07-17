'''
Conexión con la Base de Datos e inyección de datos del archivo .csv
Se busca imitar un entorno real, a baja escala y localemte.
'''

# %%
import psycopg2 as ps
import pandas as pd
from config import RAW_BANK_FRAUD


# %%
# Creemos la conexión y el cursor para las operaciones.

connection = ps.connect(dbname="mi_base_dato", 
                        user="admin", 
                        password="postgrespass",
                        host="db",
                        port="5432")

cursor = connection.cursor()

# La conexion funciona bien.
# No hay que olvidar cerrarla.

cursor.close()
connection.close()

# Fin.