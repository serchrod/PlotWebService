from flask import Flask, escape, request
from flask import send_file

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'




@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'test.png'
    else:
       filename = 'test.png'
    return send_file(filename, mimetype='image/png')