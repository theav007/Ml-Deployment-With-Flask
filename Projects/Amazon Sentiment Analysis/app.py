import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    if request.method=='POST':
        comment=request.form['review']
        data=[comment]
        prediction=model.predict(data)
        output=prediction[0]
    return render_template('index.html',
   prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)