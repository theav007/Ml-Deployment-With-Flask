import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,
    json={'sex':2, 'married':1, 'edu':0,'emp':1,'pro':2,'depent':0,
          'income':8000,'cpincome':10000,'loan':10000,'loanterm':360,
          'history':0})

print(r.json())