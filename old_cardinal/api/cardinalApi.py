
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send', methods=['POST'])
def send():
    return 'snippet sent'

@app.route('/get', methods=['GET'])
def get():
    return 'hello there'

# run the application
app.run(host='0.0.0.0', debug=True)