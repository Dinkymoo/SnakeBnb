from flask import Flask
app = Flask("Activities")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/english')
def hello_eng():
    return 'Hello, English!'

@app.route('/dutch')
def hello_dutch():
    return 'Hoi!'