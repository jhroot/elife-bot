import logging
from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)


@app.route('/notification', methods=['POST'])
def index():

    request_data = request.get_json()
    print(request_data)
    return jsonify({"result": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7473)