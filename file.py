from response import Response

class file:
    def write(path : str, type : str, content):
        with open(path, type ) as file :
            file.write(content)
            
    def read(path : str, type : str):
        with open(path, type) as file:
            return Response.custom(file.read())