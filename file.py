from response import Response

class file:
    def write(path, type, content):
        with open(path, type ) as file :
            file.write(content)
            
    def read(path, type):
        with open(path, type) as file:
            return Response.custom(file.read())