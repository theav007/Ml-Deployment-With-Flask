import numpy as np
from flask import Flask, request,render_template,jsonify
import pickle

app = Flask(__name__)

model_text = pickle.load(open('text_model.pkl', 'rb'))




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/text')
def text():
    return render_template('text.html')

@app.route('/text_predict',methods=['POST'])
def text_predict():

    text =request.form["name"]
    #final_features = np.array(int_features)
    prediction = model_text.predict([text])
    result=str(prediction)
 
    if text:
        msg = result
        return jsonify({'name' : msg})
 
    return jsonify({'error' : 'Missing data!'})




if __name__ == "__main__":
    app.run(debug=True)
