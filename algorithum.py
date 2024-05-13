class algorithm :
    def encrypt(publicKey, privateKey, data):
        head = publicKey
        tail = privateKey
        body = data
        return head + body + tail