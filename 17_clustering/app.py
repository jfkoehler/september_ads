from flask import Flask 
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def home():
    return 'Rhianna'

if __name__ == '__main__':
    app.run(debug = True)