from datetime import datetime
from flask import render_template,request
from datetime import datetime
from . import app
from .models import CryptoCambio, DBManager
from .forms import PurchaseForm


@app.route("/")
def inicio():
    db = DBManager('data/Cryptomovimientos.db')
    movimientos = db.querySQL(
        "SELECT  date , time, from_currency, from_quantity, to_currency, to_quantity FROM movements")
    return render_template("inicio.html", movs=movimientos)
    #return jsonify(movimientos)


@app.route("/purchase/", methods=['GET', 'POST'])
def purchase():
    
    
    if request.method=='GET':
     return render_template("purchase.html", form=PurchaseForm())
    
    elif request.method=='POST':
        form=PurchaseForm(request.form)
        
        cantidadCambiada=0
        P_U = 0
        
        aCambiar=CryptoCambio(form.from_currency.data,form.to_currency.data)
        rate= aCambiar.exchange()

        cantidadAcambiar=int(form.from_quantity.data)        
        cantidadCambiada= cantidadAcambiar * rate
       
        P_U=cantidadAcambiar/cantidadCambiada
        
        date = datetime.now().strftime('%y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')
        
        
        if form.data["submit_aceptar"]:
            
            db=DBManager('data/Cryptomovimientos.db')
            params=(date,time,form.from_currency.data,form.from_quantity.data,form.to_currency.data,cantidadCambiada)
            consulta="INSERT INTO movements (date,time,from_currency,from_quantity,to_currency,to_quantity) VALUES (?,?,?,?,?,?);"
            resultado=db.ejecutarConParametros(consulta,params)
            return  render_template("compra_ok.html",resultado=resultado)
       
        elif form.data["submit_calcular"]:
            return render_template('purchase.html',form=form, P_U=P_U,cantidadCambiada=cantidadCambiada)
       
       

@app.route("/purchase/status")
def status_inversion():
     pass
