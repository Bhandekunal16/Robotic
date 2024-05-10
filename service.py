import os, time, psutil, shutil, subprocess

class service :
    
    def write(name):
        """Writes content to a file.

        Args:
            name (str): The name of the file to write to.
        """
        with open(name, 'w') as file:
            file.write('//Hello, world!\n')
            file.write('//This is a new file created using Python.')

    def read(name):
        """Reads the contents of a file and prints them.

        Args:
            name (str): The name of the file to read.
        """
        with open(name, 'r') as file:
            contents = file.read()
            print(contents)

    def lineRead(name):
        """Reads the contents of a file line by line and prints them.

        Args:
            name (str): The name of the file to read.
        """
        with open(name, 'r') as file:
            for line in file:
                print(line.strip())
            
    def edit(name, Content):
        """Appends content to an existing file.

        Args:
            name (str): The name of the file to edit.
            Content (str): The content to append to the file.
        """
        with open(name, 'a') as file:
            file.write(Content)
            
    def mkdir(name):
        """Creates a new directory.

        Args:
            name (str): The name of the directory to create.
        """
        os.makedirs(name, exist_ok=True)
        if os.path.exists(name):
            print("Folder created successfully.")
        else:
            print("Failed to create folder.")
            
    def remove(name):
        """Removes a file.

        Args:
            name (str): The name of the file to remove.
        """
        try:
            os.remove(name)
            print("File removed successfully.")
        except OSError as e:
            print(f"Error: {name} : {e.strerror}")
            
    def rmdir(name):
        """Removes a directory.

        Args:
            name (str): The name of the directory to remove.
        """
        try:
            os.rmdir(name)
            print("Folder removed successfully.")
        except OSError as e:
            print(f"Error: {name} : {e.strerror}")
            
    def cd(name):
        """Changes the current working directory.

        Args:
            name (str): The path to the new working directory.
        """
        try:
            os.chdir(name)
            print("Current working directory changed to:", os.getcwd())
        except OSError as e:
            print(f"Error: {e.strerror}")
            
    def long_running_task():
        """Simulates a long-running task by printing progress messages."""
        for i in range(10):
            time.sleep(1)  
            print(f"Progress: {i+1}/10")
            
    def memory():
        """Prints information about memory usage."""
        mem = psutil.virtual_memory()
        print(f"Total Memory: {mem.total} bytes")
        print(f"Available Memory: {mem.available} bytes")
        print(f"Used Memory: {mem.used} bytes")
        print(f"Free Memory: {mem.free} bytes")
        
    def cpu():
        """Prints information about CPU usage."""
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        
    def copy(source, destination):
        """Copies a file from source to destination.

        Args:
            source (str): The path to the source file.
            destination (str): The path to the destination file.
        """
        shutil.copy(source, destination)

    def rename(old_name, new_name):
        """Renames a file.

        Args:
            old_name (str): The current name of the file.
            new_name (str): The new name for the file.
        """
        os.rename(old_name, new_name)
        
    def chmod(name):
        """Changes the permissions of a file.

        Args:
            name (str): The name of the file to modify.
        """
        os.chmod(name, 0o755)
        
    def list(name):
        """Lists the contents of a directory.

        Args:
            name (str): The name of the directory to list.
        """
        contents = os.listdir(name)
        print(contents)
        
            
    def temperature():
        """Prints CPU temperatures."""
        temperatures = psutil.sensors_temperatures()
        if temperatures:
            print("CPU Temperatures:")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
                
    def bootTime():
        """Prints the system boot time."""
        data = psutil.boot_time()
        print(data)
        
    def getloadavg():
        """Prints system load averages."""
        data = psutil.getloadavg()
        print(data)
        
    def net_connections():
        """Prints network connections."""
        data = psutil.net_connections()
        print(data)
        
    def address():
        """Prints network interface addresses."""
        data = psutil.net_if_addrs()
        print(data)
    
    def stats():
        """Prints network interface statistics."""
        data = psutil.net_if_stats()
        print (data)
        
    def counters():
        """Prints network I/O counters."""
        data = psutil.net_io_counters()
        print(data)
        
    def pids():
        """Prints active process IDs."""
        data = psutil.pids()
        print(data)
        
    def battery():
        """Prints battery information."""
        data = psutil.sensors_battery()
        print(data)
        
    def fans():
        """Prints fan speeds."""
        data = psutil.sensors_fans()
        print(data)
        
    def user():
        """Prints information about active users."""
        data = psutil.users()
        print(data)
        
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def node(name):
        subprocess.run(['node', name], capture_output=True, text=True)