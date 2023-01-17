from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
c = CurrencyRates()


app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdefg"
debug = DebugToolbarExtension(app)
app.debug = False

symbols = {"USD":"&dollar;","EUR":"&euro;","GBP":"&pound;",
"CAD":"&dollar;", "AUD":"&dollar;","JPY":"&yen;","INR":"&#8377;",
"NZD":"&dollar;","CHF":"&#8355;","ZAR":"&#82;","SGD":"&dollar;",
"HKD":"&dollar;","CNY":"&#20803;","MXN":"&#8369;","BRL":"&#82;&#36;",
"PHP":"&#8369;","IDR":"&#82;&#112;","KRW":"&#8361;","TRY":"&#8378;"}


@app.route('/')
def show_home():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def show_convert():
    try: 
        base_cur = request.form['from']
        dest_cur = request.form['to']
        amount = float(request.form['amount'])
        symbol_one = symbols[base_cur]
        symbol_two = symbols[dest_cur]

        result = c.convert(base_cur, dest_cur, amount)
        return render_template('convert.html', base_cur= base_cur, dest_cur=dest_cur,
        amount=f'{amount:,}',result=f'{result:,.2f}', symbol_one=symbol_one,symbol_two=symbol_two)

    except(TypeError, KeyError, ValueError):
        error_message= "All Inputs Are Required And Amount Must Be An Integer"
        return render_template('index.html',error_message=error_message)

   

