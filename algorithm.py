from service import service
import base64, hashlib, re


class algorithm:
    def encrypt(publicKey, privateKey, data):
        tail : str = service.hex(publicKey)
        head : str = service.hex(privateKey)
        body : str = base64.b64encode(data.encode()).decode()
        combined_string : str = tail
        hashed_string : str = hashlib.sha256(combined_string.encode()).hexdigest()
        return head + body + hashed_string

    def decrypt(publicKey, privateKey, data):
        tail = service.hex(publicKey)
        head = service.hex(privateKey)
        hashed_string = hashlib.sha256(tail.encode()).hexdigest()
        data

        modified_string = re.escape(head)
        nextModified_string = re.escape(hashed_string)

        newString = data.replace(modified_string, "")
        nextNewString = newString.replace(nextModified_string, "")

        decoded_data = base64.b64decode(nextNewString.encode()).decode()

        return decoded_data
