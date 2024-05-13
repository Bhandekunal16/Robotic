from algorithm import algorithm

obj = {
        'name' : 'yash', 
       'array': ['q', '2', 'm', 'n']
       }


def main():
    data = algorithm.encrypt('username', 'robotic', obj)
    print(data)
    

main()