from flask import Flask, render_template, request, session
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdefg"
