from service import service
import os


def application():
        current_file_path = os.path.abspath(__file__)
        task : str = input(f'{current_file_path}$:')
        if task == 'write':
            newTask : str = input('enter file name :')
            service.write(newTask)
        elif task == 'read':
            newTask : str = input('enter file name :')
            service.read(newTask)
        elif task == 'readline':
            newTask : str = input('enter file name :')
            service.read(newTask)
        elif task == 'edit':
            newTask : str = input('enter file name :')
            content : str = input('enter content :')
            service.edit(newTask, content)
        elif task == 'mkdir':
            newTask : str = input('enter folder name :')
            service.mkdir(newTask)
        elif task == 'remove':
            newTask : str = input('enter folder name :')
            service.remove(newTask)
        elif task == 'rmdir':
            newTask : str = input('enter folder name :')
            service.rmdir(newTask)
        elif task == 'cd':
            newTask : str = input('enter folder name :')
            service.cd(newTask)
        elif task == 'simulate':
            service.long_running_task()
        elif task == 'memory':
            service.memory()
        elif task == 'cpu':
            service.cpu()
        elif task == 'exit':
            'exit'
        elif task == 'copy':
            newTask : str = input('enter file name :')
            newTask2 : str = input('enter destination for the file :')
            service.copy(newTask, newTask2 )
        elif task == 'rename':
            newTask : str = input('enter old file name :')
            newTask2 : str = input('enter new file name :')
            service.copy(newTask, newTask2 )
        elif task == 'chmod':
            newTask : str = input('enter file name :')
            service.chmod(newTask)
        elif task == 'li':
            newTask : str = input('enter file name :')
            service.list(newTask)
        elif task == 'temperature':
            service.temperature()
        elif task == 'boot':
            service.bootTime()
        elif task == 'unknown':
            service.getloadavg()
        elif task == 'net':
            service.net_connections()
        elif task == 'address':
            service.address()
        elif task == 'stats':
            service.stats()
        elif task == 'counter':
            service.counters()

application()