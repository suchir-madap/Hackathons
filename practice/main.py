


from flask import Flask, jsonify, request
from pymongo import MongoClient, operations

app = Flask(__name__)

#create our routes

@app.route('/home', methods=['POST'])
def register():
    data = request.get_json()
    client = MongoClient('mongodb+srv://flimiso12:flimiso12@cluster0.hwuin.mongodb.net/FLI?retryWrites=true&w=majority')
    db = client['FLI']
    collection = db['users']

    post = {'username': data['username'], 'password': data['password']}
    collection.insert_one(post)
    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    client = MongoClient('mongodb+srv://flimiso12:flimiso12@cluster0.hwuin.mongodb.net/FLI?retryWrites=true&w=majority')
    db = client['FLI']
    collection = db['users']


    post = {'username': data['username'], 'password': data['password']}
    if collection.find_one(post):
        return jsonify({'success': True})
    
    else:
        return jsonify({'success': False})



app.run(host = '0.0.0.0')
