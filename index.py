from service import service
from color import Color
import os


def application():
    """
    application that sort the os function according your choice and do your work
    """
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    os.environ['PATH'] += os.pathsep + current_file_path
    task = input( f'Welcome to the mystical castle of {os.getcwd()}. What would you like to explore today?:\n' + Color.RESET)

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
            return 'exit'
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
        case  'ls':
            current_dir = current_dir = os.getcwd()
            service.list(current_dir)
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
        case 'clear':
            service.clear()
        case 'node c':
            newTask : str = input('enter file name :')
            service.node(newTask)
        case 'permission':
            service.permission()
        case 'python --v':
            service.version()

def tasks():
    try :
        while True:
            print(Color.MAGENTA + '*************************' + Color.CYAN)
            result = application()
            if result == 'exit':
                print(Color.MAGENTA + '********** thank you! ***********')
                break
    except OSError as e:
            print(Color.RED + f"Error: {e.strerror}")
            tasks()
        
tasks()