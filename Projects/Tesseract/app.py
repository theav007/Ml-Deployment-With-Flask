import numpy as np
from flask import Flask, request,render_template,jsonify
from PIL import Image
import pytesseract as py
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/tesseract',methods=['POST'])
def tesseract():
    file = request.files['image']
    extension = os.path.splitext(file.filename)[1]
    oldname = os.path.splitext(file.filename)[0]
    f_name=oldname+extension
    app.config['UPLOAD_FOLDER'] = 'static/upload'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
    
    ipath='static/upload'
    img_path=os.path.join(ipath, f_name)
    tesseract_image=Image.open(img_path)
    text=py.image_to_string(tesseract_image)
    return render_template('index.html',
                           prediction_image=text)
    



if __name__ == "__main__":
    app.run(debug=True)
