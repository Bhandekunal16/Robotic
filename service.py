import os, time, psutil, shutil, subprocess, sys, struct, tempfile
from color import Color
from response import Response
from file import file
from Global import string


class service:
    def __init__(self):
        pass

    def write(path: str):
        file.write(path, "w", string.initialFileContent)

    def touch(path: str):
        command = path.split()
        file.write(
            command[1],
            "w",
            string.initialFileContent,
        )

    def read(path: str):
        file.read(path, "r")

    def cat(path: str):
        command = path.split()
        file.read(command[1], "r")

    def lineRead(path: str):
        with open(path, "r") as file:
            for line in file:
                print(line.strip())

    def edit(path: str, content):
        file.write(path, "a", content)

    def mkdir(path: str):
        os.makedirs(path, exist_ok=True)
        if os.path.exists(path):
            print(string.folderCreatedSuccessfully)
        else:
            print(string.failToCreate)

    def remove(path: str):
        try:
            os.remove(path)
            print(Color.GREEN + string.removeFolder)
        except OSError as e:
            print(Color.RED + f"{string.Error} : {path} : {e.strerror}")

    def rmdir(path: str):
        try:
            os.rmdir(path)
            print(Color.GREEN + string.removeFolder)
        except OSError as e:
            print(Color.RED + f"{string.Error} : {path} : {e.strerror}")

    def long_running_task():
        for i in range(10):
            time.sleep(1)
            print(f"Progress: {i+1}/10")

    def memory():
        mem = psutil.virtual_memory()
        print(
            f"{string.TotalMemory} {mem.total} {string.bytes}\n {string.AvailableMemory} {mem.available} {string.bytes}\n {string.UsedMemory} {mem.used} {string.bytes}\n {string.FreeMemory} {mem.free} {string.bytes}\n"
        )

    def cpu():
        print(f"{string.CPUUsage} {psutil.cpu_percent()}%")

    def copy(source, destination):
        shutil.copy(source, destination)

    def rename(old_name, new_name):
        os.rename(old_name, new_name)

    def chmod(name):
        os.chmod(name, 0o755)

    def list(self, name, indent=""):
        items = os.listdir(name)
        print(Color.RESET + 'total item :' + str(len(items)))
        for item in sorted(items):
            print(Color.YELLOW + "-" * 100 + Color.RESET)
            full_path = os.path.join(name, item)
            if os.path.isdir(full_path):
                print(Color.RESET + f"{indent}folder     : {item}/" )
                nextItems = os.listdir(item)
                print(Color.RESET + 'total item :' + str(len(nextItems)))
                print("-" * 47 + 'folder' + "-" * 48)
                if len(nextItems) == 0:
                    print(" " * 45 + 'Empty folder' + " " * 45)
                for Item in sorted(nextItems):
                    new_full_path = os.path.join(name, Item)
                    if os.path.isdir(new_full_path):
                        print(f"{indent}+--{new_full_path}/{Item}")
                    else:
                        print(Color.YELLOW +f"{indent}     ./{Item}" + Color.RESET )
                print("-" * 48 + ' END ' + "-" * 48)
            else:
                print(f"{indent} {item}")

    def temperature():
        temperatures = psutil.sensors_temperatures()
        if temperatures:
            print(string.CPUTemperatures)
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current} {string.C}")

    def bootTime():
        Response.custom(psutil.boot_time())

    def getloadavg():
        Response.custom(psutil.getloadavg())

    def net_connections():
        Response.custom(psutil.net_connections())

    def address():
        Response.custom(psutil.net_if_addrs())

    def stats():
        Response.custom(psutil.net_if_stats())

    def counters():
        Response.custom(psutil.net_io_counters())

    def pids():
        Response.custom(psutil.pids())

    def battery():
        Response.custom(psutil.sensors_battery())

    def fans():
        Response.custom(psutil.sensors_fans())

    def user():
        data = psutil.users()
        obj = {"name": data[0].name, "host": data[0].host, "terminal": data[0].terminal}
        Response.custom(obj)

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def node(name):
        data = subprocess.run(["node", name], capture_output=True, text=True)
        Response.custom(data.stdout)

    def permission():
        path = os.getcwd()
        per = os.stat(path)
        code = str(per.st_mode)
        if code.find("689"):
            print(string.permissionFound)
        print(per.st_mode)

    def version():
        current_version = sys.version_info
        if current_version >= (3, 8):
            print(
                f"Version {current_version.major}.{current_version.minor}.{current_version.micro}"
            )

    def generate(name):
        command = name.split()
        data = subprocess.run(
            [command[0], command[1], command[2], command[3]], check=True
        )
        print(data.stdout)

    def versions(part1, part2):
        data = subprocess.run([part1, part2], capture_output=True, text=True)
        print(data.stdout)

    def ping(name):
        command = name.split()
        result = subprocess.run(
            [command[0], "-c", "4", command[1]], capture_output=True, text=True
        )
        print(result.stdout)

    def cd(name):
        try:
            command = name.split()
            os.chdir(command[1])
            print(Color.GREEN + string.currentDirectory, os.getcwd())
        except OSError as e:
            print(f"Error: {e.strerror}")

    def shutdown():
        os.system("shutdown -h now")

    def restart():
        os.system("shutdown -r now")

    def search(folder, filename):
        found_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file == filename:
                    found_files.append(os.path.join(root, file))
        if found_files:
            print(string.fileFound)
            for file_path in found_files:
                print(file_path)
        else:
            print(string.fileNotFound)

    def process():
        print(os.getpid())

    def random(number):
        print(os.urandom(number))

    def binaryConverter(data):
        if type(data) == str:
            binary_str = "".join(format(ord(char), "08b") for char in data)
            print(binary_str)
            return binary_str
        elif type(data) == int:
            binary_str = bin(data)
            print(string.BinaryRepresentationOf, data, "is:", binary_str)
            return binary_str
        elif type(data) == float:
            packed = struct.pack("!d", data)
            binary_str = "".join(f"{x:08b}" for x in packed)
            print(string.BinaryRepresentationOf, data, "is:", binary_str)
            return binary_str

    def binaryRepresentation(name):
        with open(name, "rb") as File:
            binary_data = File.read()
            binary_str = "".join(f"{byte:08b}" for byte in binary_data)
            file.write(f"./bin/{name}.bin", "w", binary_str)
            return binary_data

    def hex(data):
        hexadecimal_str = data.encode().hex()
        return hexadecimal_str

    def decodeHex(data):
        output = bytes.fromhex(data).decode()
        return output

    def nano(path):
        command = path.split()
        with open(command[1], "r") as file:
            content = file.read()
        with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_file:
            temp_file.write(content)
            temp_file_name = temp_file.name
            subprocess.call(["nano", temp_file_name])
        with open(temp_file_name, "r") as temp_file:
            edited_content = temp_file.read()
        with open(path, "w") as original_file:
            original_file.write(edited_content)
