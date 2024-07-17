from service import service
from color import Color
import os
from algorithm import algorithm
from environment import environment
from Global import string


class module:
    def application(task):
        match task:
            case "write":
                name: str = input(string.enterFileName)
                service.write(name)
            case "read":
                name: str = input(string.enterFileName)
                service.read(name)
            case "readline":
                name: str = input(string.enterFileName)
                service.lineRead(name)
            case "edit":
                name: str = input(string.enterFileName)
                content: str = input(string.enterContent)
                service.edit(name, content)
            case "simulate":
                service.long_running_task()
            case "memory":
                service.memory()
            case "cpu":
                service.cpu()
            case "exit":
                return "exit"
            case "ls":
                current_dir = current_dir = os.getcwd()
                service.list("", current_dir)
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
            case "permission":
                service.permission()
            case "python --v":
                service.version()
            case "heavyTask":
                newTask: str = input(string.enterTask)
                service.generate(newTask)
            case "shutdown":
                service.shutdown()
            case "restart":
                service.restart()
            case "search":
                name: str = input(string.enterFileName)
                folder: str = os.getcwd()
                service.search(folder, name)
            case "process":
                service.process()
            case "random":
                length: int = int(input(string.enterLengthForString))
                service.random(length)
            case "binary":
                print(string.suggestion)
                type = input(string.enterData)
                if type == "str":
                    enter = input(string.enterData)
                    service.binaryConverter(enter)
                elif type == "int":
                    enter = int(input(string.enterData))
                    service.binaryConverter(enter)
                elif type == "float":
                    enter = float(input(string.enterData))
                    service.binaryConverter(enter)
            case "represent":
                name = input(string.enterFileName)
                service.binaryRepresentation(name)
            case "hex-decimal":
                print(string.qus1)
                type = input(string.enterData)
                if type == "encode":
                    convert = input(string.enterData)
                    service.hex(convert)
                elif type == "decode":
                    convert = input(string.enterData)
                    service.decodeHex(convert)
            case "encrypt":
                publicKey = input(string.enterPublicKey)
                privateKey = environment.privateKey
                data = input(string.enterData)
                data = algorithm.encrypt(publicKey, privateKey, data)
                print(data)
            case "decrypt":
                publicKey = input(string.enterPublicKey)
                privateKey = environment.privateKey
                data = input(string.enterData)
                data = algorithm.decrypt(publicKey, privateKey, data)
                print(data)
            case _:
                print(Color.RED + f"Command {task} not found!")


def tasks():
    try:
        while True:
            half = "*" * 69
            header = "*" * 149
            print(Color.GREEN + header), print(Color.CYAN + string.welcome), print(
                Color.GREEN + header
            )
            current_file_path = os.path.dirname(os.path.abspath(__file__))
            os.environ["PATH"] += os.pathsep + current_file_path
            task = input(
                Color.GREEN
                + f"Welcome to the mystical castle of{Color.CYAN } {os.getcwd()}.{Color.GREEN }What would you like to explore today?:\n"
                + Color.GREEN
            )
            if "cd" in task:
                service.cd(task)
            elif "cat" in task:
                service.cat(task)
            elif "touch" in task:
                service.touch(task)
            elif "nano" in task:
                service.nano(task)
            elif "ping" in task:
                service.ping(task)
            elif "node" in task:
                command: str = task.split()
                service.node(command[1])
            elif "mkdir" in task:
                command: str = task.split()
                service.mkdir(command[1])
            elif "remove" in task:
                command: str = task.split()
                service.remove(command[1])
            elif "rmdir" in task:
                command: str = task.split()
                service.rmdir(command[1])
            elif "rename" in task:
                command: str = task.split()
                service.rename(command[1], command[3])
            elif "copy" in task:
                command: str = task.split()
                service.copy(command[1], command[3])
            elif "chmod" in task:
                command: str = task.split()
                service.chmod(command[1])
            elif "run" in task:
                command: str = task.split()
                service.versions(command[1], command[2])
            elif 'format' in task :
                command: str = task.split()
                service.format(command[1])
            else:
                result = module.application(task)
                if result == "exit":
                    print(Color.GREEN + half + string.thankYou + half)
                    break
    except OSError as e:
        print(Color.RED + f"Error: {e.strerror}")
        tasks()


tasks()
