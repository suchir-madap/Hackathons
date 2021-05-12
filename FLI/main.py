


from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient, operations

app = Flask(__name__)

#create our routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/events', methods = ['POST', 'GET'])
def events():
    return 'events'

@app.route('/meetings', methods = ['POST', 'GET'])
def meetings():
    return 'meetings'

@app.route('/officers', methods = ['POST', 'GET'])
def officers():
    return 'officers'

@app.route('/join_us', methods = ['POST', 'GET'])
def join_us():
    return 'join_us'

@app.route('/contact_us', methods = ['POST', 'GET'])
def contact_us():
    return 'contact_us'

@app.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    client = MongoClient('mongodb+srv://flimiso12:flimiso12@cluster0.hwuin.mongodb.net/FLI?retryWrites=true&w=majority')
    db = client['FLI']
    collection = db['users']

    def register_m():
        post = {"username": data["username"], "password": data["password"]}
        if collection.find_one(post):
            return jsonify({"success": True})
    
        else:  
            return jsonify({"success": False})
        
    
    def login_m():
        post = {"username": data["username"], "password": data["password"]}
        if collection.find_one(post):
            return jsonify({"success": True})
        
        else:
            return jsonify({"success": False})



app.run(host = '0.0.0.0', debug = True)
