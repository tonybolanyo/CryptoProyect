
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import HiddenField, SubmitField,DecimalField
from wtforms.validators import DataRequired


class PurchaseForm(FlaskForm):

    id =HiddenField()
    lista_from = SelectField( "From", choices = [("EUR","Euro"),("BTC","Bitcoin"),("ETH","Ether"),("USDT","Tether"),("ADA","Cardano"),("SOL","Solana"),("XRP","Ripple"), ("DOT","Polkadot"),("DOGE","Dogecoin"),("SHIB","Shibs_Inu")])
    lista_to = SelectField("To", choices = [("EUR","Euro"),("BTC","Bitcoin"),("ETH","Ether"),("USDT","Tether"),("ADA","Cardano"),("SOL","Solana"),("XRP","Ripple"), ("DOT","Polkadot"),("DOGE","Dogecoin"),("SHIB","Shibs_Inu")] )                                                                                               
    cantidad= DecimalField ("Q", validators=[DataRequired(message="Debes indicar una cantidad")],places=2)
       
   # FloatField ( argumentos de campo predeterminados )
    submit_calcular=SubmitField("Calcular")
    submit_aceptar= SubmitField("Enviar")