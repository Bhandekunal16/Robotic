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
        response = algorithm.encrypt(public_key, privateKey, data)
        return jsonify({'encryptedData': response}), 200

@app.route('/decrypt', methods=['POST'])
def decrypt():
    privateKey = "robotic"
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