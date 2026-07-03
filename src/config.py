'''
Archivo de Configuración de Rutas
'''

from pathlib import Path

# Paths a directorios importantes.

SRC_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = SRC_DIR.parent

DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW_DIR = DATA_DIR / "raw"

# Paths a DataSets

RAW_BANK_FRAUD = DATA_RAW_DIR / "bank_fraud.csv"


# Fin.