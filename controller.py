from flask import Flask, request, jsonify
from algorithm import algorithm
from route import Route
from environment import environment 
from response import Response

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
        return Response.encryption(response)

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
            return Response.notfound(f'{public_key} is matched with your public key')
        else :
            return Response.decryption(response)

if __name__ == '__main__':
    app.run(debug=True)