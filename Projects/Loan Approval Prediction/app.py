import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    if int(output)==1:
        prediction1="Yes!!! You Are Eligible For This Loan"
    else:
        prediction1="No You Are Not Eligible For This Loan"
    return render_template('index.html',
   prediction_text=prediction1)


if __name__ == "__main__":
    app.run(debug=True)