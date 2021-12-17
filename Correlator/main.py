import psycopg2
import pandas as pd

import matplotlib.pyplot as plt


def ejecutar_sql( par ):

    # se conecta a la base de datos
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='mysecretpassword',
        database='postgres')

    # ejecuta SQL y cierra conexion.
    sql_string = "SELECT precio, fechahora hora from tablaprecios where par = '" + par + "'"

    cursor = connection.cursor()
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    datos_ejes = pd.DataFrame(columns=['precio', 'fechahora'])
    for fila in rows:
        datos_ejes = datos_ejes.append({ 'precio': fila[0], 'fechahora': fila[1]}, ignore_index=True)

    connection.close()

    return  datos_ejes

# guardo los datos de los ejes de cada moneda
df_datos_btc = ejecutar_sql('BTCUSDT')
df_datos_eth = ejecutar_sql('ETHUSDT')
df_datos_doge = ejecutar_sql('DOGEUSDT')

#normalizo todos los precios
df_datos_btc["precio"] = (df_datos_btc["precio"]-df_datos_btc["precio"].min()) / (df_datos_btc["precio"].max()-df_datos_btc["precio"].min())
df_datos_eth["precio"] = (df_datos_eth["precio"]-df_datos_eth["precio"].min()) / (df_datos_eth["precio"].max()-df_datos_eth["precio"].min())
df_datos_doge["precio"] = (df_datos_doge["precio"]-df_datos_doge["precio"].min()) / (df_datos_doge["precio"].max()-df_datos_doge["precio"].min())

#armamos los ejes para el grafico btc
y_data_btc = df_datos_btc["precio"].tolist()
x_data_btc = df_datos_btc["fechahora"].tolist()

#armamos los ejes para el grafico eth
y_data_eth = df_datos_eth ["precio"].tolist()
x_data_eth = df_datos_eth ["fechahora"].tolist()

#armamos los ejes para el grafico doge
y_data_doge = df_datos_doge["precio"].tolist()
x_data_doge = df_datos_doge["fechahora"].tolist()

plt.plot(x_data_btc, y_data_btc, label='BTCUSDT')
plt.plot(x_data_eth, y_data_eth, label='ETHUSDT')
plt.plot(x_data_doge, y_data_doge, label='DOGEUSDT')

plt.show()


