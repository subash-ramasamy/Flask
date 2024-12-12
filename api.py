from flask import Flask

app = Flask(__name__)

# API endpoints

@app.route('/', methods = ['GET'])
def hello_world():
    return "<h1>  Hello there...!! </h1>"

@app.route('/ping', methods = ['GET'])
def ping():
    return {"message": "why are you pinging me??"}  



