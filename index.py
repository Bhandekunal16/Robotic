from service import service
from color import Color
import os
from algorithm import algorithm


class module:
    def application(task):
        """
        application that sort the os function according your choice and do your work
        """
        match task:
            case "write":
                newTask: str = input("enter file name :")
                service.write(newTask)
            case "read":
                newTask: str = input("enter file name :")
                service.read(newTask)
            case "readline":
                newTask: str = input("enter file name :")
                service.lineRead(newTask)
            case "edit":
                newTask: str = input("enter file name :")
                content: str = input("enter content :")
                service.edit(newTask, content)
            case "mkdir":
                newTask: str = input("enter folder name :")
                service.mkdir(newTask)
            case "remove":
                newTask: str = input("enter folder name :")
                service.remove(newTask)
            case "rmdir":
                newTask: str = input("enter folder name :")
                service.rmdir(newTask)
            case "simulate":
                service.long_running_task()
            case "memory":
                service.memory()
            case "cpu":
                service.cpu()
            case "exit":
                return "exit"
            case "copy":
                newTask: str = input("enter file name :")
                newTask2: str = input("enter destination for the file :")
                service.copy(newTask, newTask2)
            case "rename":
                newTask: str = input("enter old file name :")
                newTask2: str = input("enter new file name :")
                service.copy(newTask, newTask2)
            case "chmod":
                newTask: str = input("enter file name :")
                service.chmod(newTask)
            case "ls":
                current_dir = current_dir = os.getcwd()
                service.list(current_dir)
            case "temperature":
                service.temperature()
            case "boot":
                service.bootTime()
            case "unknown":
                service.getloadavg()
            case "net":
                service.net_connections()
            case "address":
                service.address()
            case "stats":
                service.stats()
            case "counter":
                service.counters()
            case "pid":
                service.pids()
            case "battery":
                service.battery()
            case "fans":
                service.fans()
            case "users":
                service.user()
            case "clear":
                service.clear()
            case "node c":
                newTask: str = input("enter file name :")
                service.node(newTask)
            case "permission":
                service.permission()
            case "python --v":
                service.version()
            case "task":
                newTask: str = input("enter the task :")
                service.versions(newTask)

            case "shutdown":
                service.shutdown()

            case "restart":
                service.restart()

            case "search":
                newTask: str = input("enter file name :")
                folder: str = os.getcwd()
                service.search(folder, newTask)

            case "process":
                service.process()

            case "random":
                newTask: int = int(input("enter length for string :"))
                service.random(newTask)

            case "binary":
                print("suggested type (str, int, float)")
                newTask = input("enter type of input data:")

                if newTask == "str":
                    enter = input("enter your data :")
                    service.binaryConverter(enter)
                elif newTask == "int":
                    enter = int(input("enter your data :"))
                    service.binaryConverter(enter)
                elif newTask == "float":
                    enter = float(input("enter your data :"))
                    service.binaryConverter(enter)

            case "represent":
                newTask = input("enter the file name :")
                service.binaryRepresentation(newTask)
                
            case 'hex-decimal':
                print("what process you want?")
                newTask = input("enter type of input data:")
                if newTask == 'encode':
                    newTask2 = input("enter your data :")
                    service.hex(newTask2)
                elif newTask == 'decode':
                    newTask2 = input("enter your data :")
                    service.decodeHex(newTask2)
                    
            case 'encrypt':
                publicKey = input('enter your publicKey :')
                privateKey = 'robotic'
                data = input('enter you data :')
                data = algorithm.encrypt(publicKey, privateKey, data) 
                print(data)
                    


def tasks():
    try:
        while True:
            print(
                Color.MAGENTA
                + "************************************************************************"
                + Color.CYAN
            )
            current_file_path = os.path.dirname(os.path.abspath(__file__))
            os.environ["PATH"] += os.pathsep + current_file_path
            task = input(
                Color.YELLOW
                + f"Welcome to the mystical castle of{Color.CYAN } {os.getcwd()}.{Color.YELLOW }What would you like to explore today?:\n"
                + Color.RESET
            )
            if "cd" in task:
                service.cd(task)
                result = module.application(task)
            else:
                result = module.application(task)
                if result == "exit":
                    print(Color.MAGENTA + "********** thank you! ***********")
                    break
    except OSError as e:
        print(Color.RED + f"Error: {e.strerror}")
        tasks()


tasks()
