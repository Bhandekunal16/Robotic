from service import service

class algorithm :
    def encrypt(publicKey, privateKey, data):
        tail = service.hex(publicKey)
        head = service.hex(privateKey)
        body = service.binaryConverter(data)
        return head + body + tail