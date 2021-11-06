import requests
import sqlite3

API_KEY=' 4518A301-0F5B-4312-9BBB-870CBCFB8FF7'
URL ="https://rest.coinapi.io/v1/exchangerate/<from>/<to>?apikey=<API_KEY>"
        #"https://rest.coinapi.io/v1/exchangerate/{cryproig}/{crypdest}"



class APIError(Exception):
    pass

class DBManager:
    def __init__(self,ruta,):
         self.ruta=ruta
         
          

    def exchange(self,crypfrom,crypto):
        cabecera={
            "X-CoinAPI-Key": API_KEY
        }
       
        url= URL.format(crypfrom,crypto)
        respuesta= requests.get(url,header=cabecera)

        if respuesta.status_code==200:
            self.cambio=respuesta.jason()
        else:
            raise APIError(
                "ha ocurrido un error{} al consultar la API".format(respuesta.status_code))
                
       

    def querySQL(self,consulta):
        conexion =sqlite3.connect(self.ruta)
        cursor= conexion.cursor()
        cursor.execute(consulta)
        
        self.movimientos=[]
        nombre_columna=[]
        for tupla in cursor.description:
            nombre_columna.append(tupla[0])

        datos =cursor.fetchall()
        for tupla in datos:
            mov={}
            indice=0
            for nombre in nombre_columna:
                mov[nombre]=tupla[indice]
                indice +=1
            self.movimientos.append(mov)

        conexion.close()
        return self.movimientos
