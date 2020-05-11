import numpy as np
from flask import Flask, request,render_template,jsonify
import pickle
model_hr = pickle.load(open('hr_model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/hr',methods=['POST'])
def hr():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_hr.predict(final_features)

    output = prediction[0]
    if int(output)==1:
        prediction1="Yes!!! You Are Eligible For Promotion"
    else:
        prediction1="No You Are Not Eligible For Promotion"
    return render_template('index.html',
   prediction_text=prediction1)



if __name__ == "__main__":
    app.run(debug=True)
