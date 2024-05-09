import os
import time
import psutil
import shutil

class service :
    def write(name):
        with open(name, 'w') as file:
            file.write('//Hello, world!\n')
            file.write('//This is a new file created using Python.')

    def read(name):
        with open(name, 'r') as file:
            contents = file.read()
            print(contents)

    def lineRead(name):
        with open(name, 'r') as file:
            for line in file:
                print(line.strip())
            
    def edit(name, Content):
        with open(name, 'a') as file:
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
            print("File removed successfully.")
        except OSError as e:
            print(f"Error: {name} : {e.strerror}")
            
    def rmdir(name):
        try:
            os.rmdir(name)
            print("Folder removed successfully.")
        except OSError as e:
            print(f"Error: {name} : {e.strerror}")
            
    def cd(name):
        try:
            os.chdir(name)
            print("Current working directory changed to:", os.getcwd())
        except OSError as e:
            print(f"Error: {e.strerror}")
            
    def long_running_task():
        for i in range(10):
            time.sleep(1)  
            print(f"Progress: {i+1}/10")
            
    def memory():
        mem = psutil.virtual_memory()
        print(f"Total Memory: {mem.total} bytes")
        print(f"Available Memory: {mem.available} bytes")
        print(f"Used Memory: {mem.used} bytes")
        print(f"Free Memory: {mem.free} bytes")
        
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
        print(contents)
        
            
    def temperature():
        temperatures = psutil.sensors_temperatures()
        if temperatures:
            print("CPU Temperatures:")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
                
    def bootTime():
        data = psutil.boot_time()
        print(data)
        
    def getloadavg():
        data = psutil.getloadavg()
        print(data)
        
    def net_connections():
        data = psutil.net_connections()
        print(data)
        
    def address():
        data = psutil.net_if_addrs()
        print(data)
    
    def stats():
        data = psutil.net_if_stats()
        print (data)
        
    def counters():
        data = psutil.net_io_counters()
        print(data)
        
    def pids():
        data = psutil.pids()
        print(data)
        
    def battery():
        data = psutil.sensors_battery()
        print(data)
        
    def fans():
        data = psutil.sensors_fans()
        print(data)