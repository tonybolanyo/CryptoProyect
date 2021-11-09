import requests
from flask import render_template, request,jsonify

from Principal.forms import PurchaseForm
from . import app
from .models import DBManager
from .forms import PurchaseForm


@app.route("/")
def inicio():
    db = DBManager('data/Cryptomovimientos.db')
    movimientos = db.querySQL(
        "SELECT  date , time, from_currency, from_quantity, to_currency, to_quantity FROM MOVEMENTS")
    return render_template("inicio.html", movs=movimientos)
    #return jsonify(movimientos)


@app.route("/purchase/", methods=['GET', 'POST'])
def purchase():
    form= PurchaseForm(request.form)
   
    if request.method=='GET':
     return render_template("purchase.html", form=form )
    
    elif request.method== 'POST':
     return render_template("purchase.html", form=PurchaseForm)
    else:
      return 'ha ocurrido un error'



@app.route("/purchase/status")
def status_inversion():
    pass
