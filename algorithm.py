from service import service

class algorithm :
    def encrypt(publicKey, privateKey, data):
        head = service.hex(publicKey)
        tail = service.hex(privateKey)
        body = data
        print(head, body, tail)
        return head + body + tail