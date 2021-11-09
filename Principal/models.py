import json
import sqlite3
import requests
from requests.sessions import Session
from . import app
from flask import jsonify
import requests 
from flask import Flask

API_KEY ='4518A301-0F5B-4312-9BBB-870CBCFB8FF7'
URL ='https://rest.coinapi.io/v1/exchangerate/<orig>/<dest>?API_KEY=<API_KEY>'

        #'https://rest.coinapi.io/v1/exchangerate/{orig}{dest}'


class CryptoCambio():
    def __init__(self, crypfrom, crypto):
        self.crypfrom = crypfrom
        self.crypto = crypto
  

    def exchange(self):
         headers = {
            "Accept": "application/json",
            "X-CoinAPI-Key": API_KEY
            
         }
         
         url = URL.format(orig=self.crypfrom, dest=self.crypto)
         session =Session()
         session.headers.update(headers)
         
         response= session.get(url)
         data=jsonify(response.text)
         return data
         
    


class APIError(Exception):
    pass

   
        
class DBManager:
    def __init__(self, ruta,):
        self.ruta = ruta

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
