from flask import Flask, jsonify
from werkzeug.routing import BaseConverter

class IdConverter(BaseConverter):
    regex = r'[a-zA-Z0-9\-]+'

app = Flask(__name__)
app.url_map.converters['id_string'] = IdConverter

@app.route('/')
def index():
    return jsonify({})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello World"})

@app.route('/hello/<id_string:id>')
def hello_id(id):
    return_id = f"MyId2-{id}"
    return jsonify({"message": "Hello World", "id": return_id})