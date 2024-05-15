import os, time, psutil, shutil, subprocess, sys, struct
from color import Color


class service:

    def write(name):
        with open(name, "w") as file:
            file.write("//Hello, world!\n")
            file.write("//This is a new file created using Python.")

    def read(name):
        with open(name, "r") as file:
            print(file.read())
            return file.read()

    def lineRead(name):
        with open(name, "r") as file:
            for line in file:
                print(line.strip())

    def edit(name, Content):
        with open(name, "a") as file:
            file.write(Content)

    def mkdir(name):
        os.makedirs(name, exist_ok=True)
        if os.path.exists(name):
            print("Folder created successfully.")
        else:
            print("Failed to create folder.")

    def remove(name):
        try:
            os.remove(name)
            print(Color.GREEN + "File removed successfully.")
        except OSError as e:
            print(f"Error: {name} : {e.strerror}")

    def rmdir(name):
        try:
            os.rmdir(name)
            print(Color.GREEN + "Folder removed successfully.")
        except OSError as e:
            print(f"Error: {name} : {e.strerror}")

    def long_running_task():
        for i in range(10):
            time.sleep(1)
            print(f"Progress: {i+1}/10")

    def memory():
        mem = psutil.virtual_memory()
        print(
            f"Total Memory: {mem.total} bytes\n Available Memory: {mem.available} bytes\n Used Memory: {mem.used} bytes\n Free Memory: {mem.free} bytes\n"
        )

    def cpu():
        print(f"CPU Usage: {psutil.cpu_percent()}%")

    def copy(source, destination):
        shutil.copy(source, destination)

    def rename(old_name, new_name):
        os.rename(old_name, new_name)

    def chmod(name):
        os.chmod(name, 0o755)

    def list(name):
        contents = os.listdir(name)
        print(Color.GREEN + ", ".join(contents))

    def temperature():
        temperatures = psutil.sensors_temperatures()
        if temperatures:
            print("CPU Temperatures:")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")

    def bootTime():
        print(psutil.boot_time())

    def getloadavg():
        print(psutil.getloadavg())

    def net_connections():
        print(psutil.net_connections())

    def address():
        print(psutil.net_if_addrs())

    def stats():
        print(psutil.net_if_stats())

    def counters():
        print(psutil.net_io_counters())

    def pids():
        print(psutil.pids())

    def battery():
        print(psutil.sensors_battery())

    def fans():
        print(psutil.sensors_fans())

    def user():
        data = psutil.users()
        obj = {"name": data[0].name, "host": data[0].host, "terminal": data[0].terminal}
        print(obj)

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def node(name):
        data = subprocess.run(["node", name], capture_output=True, text=True)
        print(data.stdout)

    def permission():
        path = os.getcwd()
        per = os.stat(path)
        code = str(per.st_mode)
        if code.find("689"):
            print("permission found : read,write")
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

    def versions(name):
        command = name.split()
        data = subprocess.run([command[0], command[1]], capture_output=True, text=True)
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
            print("Current working directory changed to:", os.getcwd())
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
            print("Found files at this location:")
            for file_path in found_files:
                print(file_path)
        else:
            print("No files found with the specified name and extension.")

    def process():
        data = os.getpid()
        print(data)

    def random(number):
        data = os.urandom(number)
        print(data)

    def binaryConverter(data):
        if type(data) == str:
            binary_str = "".join(format(ord(char), "08b") for char in data)
            print(binary_str)
            return binary_str
        elif type(data) == int:
            binary_str = bin(data)
            print("Binary representation of", data, "is:", binary_str)
            return binary_str
        elif type(data) == float:
            packed = struct.pack("!d", data)
            binary_str = "".join(f"{x:08b}" for x in packed)
            print("Binary representation of", data, "is:", binary_str)
            return binary_str

    def binaryRepresentation(name):
        with open(name, "rb") as file:
            binary_data = file.read()
            binary_str = "".join(f"{byte:08b}" for byte in binary_data)
            print("Binary representation of file", name, "is:", binary_str)
            return binary_data

    def hex(data):
        hexadecimal_str = data.encode().hex()
        return hexadecimal_str

    def decodeHex(data):
        output = bytes.fromhex(data).decode()
        return output
