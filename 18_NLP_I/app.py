from flask import Flask, render_template, request

import numpy as np
from joblib import load 
model = load('lgr_pipe.joblib')

app = Flask(__name__)

@app.route('/')
def testing():
    return 'Hi there you are home.'

@app.route('/model')
def modeling():
    return 'Hi there you are modeling.'

@app.route('/modelpredictor', methods = ["GET", "POST"])
def predictor():
    if request.method == "POST":
        review = request.form.get('review')
        pred = model.predict(np.array([review]))
        return render_template('results.html', r = pred)
    return render_template('review_form.html')

if __name__ == '__main__':
    app.run(debug=True)