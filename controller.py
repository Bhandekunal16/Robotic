from flask import Flask, request, jsonify
from algorithm import algorithm

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def get_books():
    return 'hello world'

@app.route('/encrypt', methods=['POST'])
def encrypt():
    privateKey = "robotic"
    body = request.get_json()
    if 'publicKey' in body and 'data' in body:
        public_key = body['publicKey']
        data = body['data']
        return algorithm.encrypt(public_key, privateKey, data)


if __name__ == '__main__':
    app.run(debug=True)