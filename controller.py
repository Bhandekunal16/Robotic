from flask import Flask, request, jsonify
from algorithm import algorithm
from route import Route
from environment import environment 

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def get_books():
    return 'hello world'

@app.route(Route.encrypt, methods=['POST'])
def encrypt():
    privateKey = environment.privateKey
    body = request.get_json()
    if 'publicKey' in body and 'data' in body:
        public_key = body['publicKey']
        data = body['data']
        response = algorithm.encrypt(public_key, privateKey, data)
        return jsonify({'encryptedData': response}), 200

@app.route(Route.decrypt, methods=['POST'])
def decrypt():
    privateKey = environment.privateKey
    body = request.get_json()
    if 'publicKey' in body and 'data' in body:
        public_key = body['publicKey']
        data = body['data']
        response = algorithm.decrypt(public_key, privateKey, data)
        print(response)
        if response == None :
            return jsonify({'reason': f'{public_key} is matched with your public key', 'status': False}), 404
        else :
            return jsonify({'encryptedData': response}), 200

if __name__ == '__main__':
    app.run(debug=True)