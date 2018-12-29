from flask import Flask, request, jsonify
import json


'''
with open('Data.json') as f:
    data = json.load(f)
#data["Data"].append()
del data["Data"][1]
with open('Data.json','w') as f:
    json.dump(data,f)
return jsonify(data)
'''

 


with open('Data.json') as f:
    data = json.load(f)

app = Flask(__name__)
@app.route('/login')
def login():
    d = request.get_json()
    user = d['email']
    password = d['password']
    S = 0
    c = 0
    for each in data["Data"]:
        if each["email"] == user:
            c+=1
            if each["password"] == password:
                S = 2
            else:
                S = 1
            break
    return jsonify({"value":str(S)})

@app.route('/signup')
def signup():
    d = request.get_json()
    user = d['email']
    password = d['password']
    c = 0
    for each in data["Data"]:
        if each["email"] == user:
            c+=1
            break
    if c == 0:
        data["Data"].append({"email": user, "password": password, "bidvalue": "0"})
        with open('Data.json','w') as f:
            json.dump(data,f)
        return jsonify({"value": "User Created"})
        
    else:
        return jsonify({"value": "Existing User"})



@app.route('/bid')
def bidfunct():
    d = request.get_json()
    user = d['email']
    bid = d['bidvalue']
    max = 0
    m1 = ""
    c = 0
    for each in data["Data"]:
        if each["email"] == user:
            each["bidvalue"] = int(bid)
        if int(each["bidvalue"]) > int(bid):
            c+=1
        if int(each["bidvalue"]) > max:
            max = int(each["bidvalue"])
            m1 = each["email"]
    c+=1

    return jsonify({"userRank":str(c),"userBid":bid,"firstRank":m1,"firstBid":str(max)})