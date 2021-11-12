import sqlite3
import requests


cryptomonedas=("EUR","BTC","ETH","USDT","ADA","SOL","XRP","DOT","DOGE","SHIB")
API_KEY ="68E7B045-001D-4245-B962-B4073BCE773C"
URL ="https://rest.coinapi.io/v1/exchangerate/{orig}/{dest}"



class CryptoCambio():
    def __init__(self, crypfrom, crypto):
        self.crypfrom = crypfrom
        self.crypto = crypto



    def exchange(self):
         headers = {

            "X-CoinAPI-Key": API_KEY

         }

         url = URL.format(orig=self.crypfrom, dest=self.crypto)
         response=requests.get(url,headers=headers)

         cambio = response.json()['rate']
         return cambio





class APIError(Exception):
    pass

class DBManager:
    def __init__(self, ruta,):
        self.ruta = ruta

    def ejecutarConParametros(self, consulta, params):
        conexion=sqlite3.connect(self.ruta)
        cursor= conexion.cursor()
        resultado=False
        try:
            cursor.execute(consulta,params)
            conexion.commit()
            resultado=True
        except Exception as  error:
            print(error)
            conexion.rollback()
            conexion.close()
        return resultado


    def querySQL(self, consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)

        self.movimientos = []
        nombre_columna = []
        for tupla in cursor.description:
            nombre_columna.append(tupla[0])

        datos = cursor.fetchall()
        for tupla in datos:
            mov = {}
            indice = 0
            for nombre in nombre_columna:
                mov[nombre] = tupla[indice]
                indice += 1
            self.movimientos.append(mov)

        conexion.close()
        return self.movimientos


    def Saldo(self,consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)

        saldoAcumulado = []
        for moneda in cryptomonedas:
            saldoMonedas = self.querySQL('''
                                WITH SALDO
                                AS(SELECT SUM(to_quantity) AS saldo
                                FROM movements
                                WHERE to_currency LIKE "%{}%"
                                UNION
                                SELECT -SUM(from_quantity) AS saldo
                                FROM movements
                                WHERE from_currency LIKE "%{}%")
                                SELECT SUM(saldo)
                                FROM SALDO
                                '''.format(moneda,moneda))

            saldoAcumulado.append(saldoMonedas)
        return saldoAcumulado
