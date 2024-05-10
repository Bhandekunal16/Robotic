from service import service
import os

def application():
    """
    application that sort the os function according your choice and do your work
    """
    current_file_path : str = os.path.abspath(__file__)
    task : str = input(f'{current_file_path}$:')
    match task :
        case 'write':
            newTask : str = input('enter file name :')
            service.write(newTask)
        case 'read' :
            newTask : str = input('enter file name :')
            service.read(newTask)
        case 'readline':
            newTask : str = input('enter file name :')
            service.lineRead(newTask)
        case  'edit':
            newTask : str = input('enter file name :')
            content : str = input('enter content :')
            service.edit(newTask, content)
        case  'mkdir':
            newTask : str = input('enter folder name :')
            service.mkdir(newTask)
        case  'remove':
            newTask : str = input('enter folder name :')
            service.remove(newTask)
        case  'rmdir':
            newTask : str = input('enter folder name :')
            service.rmdir(newTask)
        case  'cd':
            newTask : str = input('enter folder name :')
            service.cd(newTask)
        case  'simulate':
            service.long_running_task()
        case  'memory':
            service.memory()
        case  'cpu':
            service.cpu()
        case  'exit':
            'exit'
        case  'copy':
            newTask : str = input('enter file name :')
            newTask2 : str = input('enter destination for the file :')
            service.copy(newTask, newTask2 )
        case  'rename':
            newTask : str = input('enter old file name :')
            newTask2 : str = input('enter new file name :')
            service.copy(newTask, newTask2 )
        case  'chmod':
            newTask : str = input('enter file name :')
            service.chmod(newTask)
        case  'li':
            newTask : str = input('enter file name :')
            service.list(newTask)
        case  'temperature':
            service.temperature()
        case  'boot':
            service.bootTime()
        case  'unknown':
            service.getloadavg()
        case  'net':
            service.net_connections()
        case  'address':
            service.address()
        case  'stats':
            service.stats()
        case  'counter':
            service.counters()
        case  'pid':
            service.pids()
        case  'battery':
            service.battery()
        case  'fans':
            service.fans()
        case  'users':
            service.user()
            

# application()

def tasks():
    while True:
        application()
        
tasks()