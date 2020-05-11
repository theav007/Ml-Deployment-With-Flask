from flask_mail import Mail, Message
from flask import Flask, request,render_template,jsonify

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '<your email id ,if gmail just input username without domain name eg:email:test@gmail.com enter:test>'
app.config['MAIL_PASSWORD'] = '<your email password>'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/process",methods=['POST'])
def process():
   name = request.form["n"]
   email = request.form["e"]
   subject = request.form["s"]
   feedback = request.form["f"]
   star = request.form["r"]
   msg = Message(subject, sender = 'your email id with domain name', 
                 recipients = [email])
   msg.body = "Hello AV,\n"+feedback+".\nRating "+star+"\nFrom\n"+name
   #mail.send(msg)
   if name and email and subject and feedback and star:
       
       mail.send(msg)
       return jsonify({"result":"Sent Mail"})
       
   return jsonify({"error":"Incorrect Details"})

if __name__ == '__main__':
   app.run(debug = True)
