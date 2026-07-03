# Estado Inicial y Condiciones de los Datos Crudos

El *DataSet* cuenta con **1.000.000 filas** y **26 columnas**.

| Nombre de la Columna | Tipo de Dato |
| - | - |
| transaction_id | str |
| customer_id | str |
| transaction_date | str |
| transaction_time | str |
| hour_of_day | int64 |
| is_weekend | int64 |
| is_night_transaction | int64 |
| country | str |
| city | str |
| merchant_category | str |
| payment_method | str |
| device_type | str |
| customer_age | int64 |
| credit_score | int64 |
| account_age_years | float64 |
| account_balance | float64 |
| transaction_amount | float64 |
| num_prev_transactions | int64 |
| transaction_freq_monthly | int64 |
| distance_from_home_km | float64 |
| time_since_last_txn_hrs | float64 |
| is_international | int64 |
| failed_attempts | int64 |
| pin_change_recently | int64 |
| is_fraud | int64 |
| fraud_type | str |

### Entendiendo la Información de Columnas Particulares

Las columnas **is_weekend**, **is_night_transaction**, **is_international** e **is_fraud** vienen tipadas como `int64`. 
Esto es así porque clasifican en forma booleana con cero y uno.

La columna **failed_attempts** es un contador de la cantidad de veces que la misma transacción fue dada por fallida.

### Detalles y Consistencia en los Datos

**Valores `Null` y `NaN`**
- Más del 90% de las filas cuentan con algún `Null` entre sus columnas. Particularmente, son 944.745 filas.

La columna **transaction_id** funciona bien como *clave primaria*, ya que todos los registros son distintos entre sí.

**Columna is_fraud y fraud_type**
- Pude constatar que todas las transacciones clasificadas como *fraudulentas* tienen su correspondiente tipo especificado (en *fraud_type*).
- Se especifican 6 tipos de fraude distintos: *Synthetic Identity*, *Friendly Fraud*, *Identity Theft*, *Account Takeover*, *Phishing* y *Card Cloning*.
- Sólo el 5.5% de las transacciones totales fueron marcadas como fraudulentas.
- El *DataSet* se encuentra muy desbalanceado respecto a las transacciones fraudulentas.

Fin.