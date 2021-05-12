


from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient, operations

app = Flask(__name__)

#create our routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    client = MongoClient('mongodb+srv://flimiso12:flimiso12@cluster0.hwuin.mongodb.net/FLI?retryWrites=true&w=majority')
    db = client['FLI']
    collection = db['users']

    post = {"username": data["username"], "password": data["password"]}
    collection.insert(post)
    return jsonify({"success": True})

@app.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    client = MongoClient('mongodb+srv://flimiso12:flimiso12@cluster0.hwuin.mongodb.net/FLI?retryWrites=true&w=majority')
    db = client['FLI']
    collection = db['users']

    post = {"username": data["username"], "password": data["password"]}
    if collection.find_one(post):
        return jsonify({"success": True})
    
    else:
        return jsonify({"success": False})

@app.route('/test', methods = ['POST', 'GET'])
def test():
    return 'test'



app.run(host = '0.0.0.0', debug = True)
