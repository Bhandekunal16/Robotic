import os

# class contain os service methods.
class service :

    # class service method that create file.
    def main(name):
        with open(name, "w") as file:
            file.write(name)
        return print('your file created successfully')
    
    # class service method that create folder.
    def folder(name):
        os.makedirs(name, exist_ok=True)
        return print('folder %s created successfully' % name)

    # class service method that create folder if not present and create file.   
    def writeDirectory(directory, fileName):
        os.makedirs(directory, exist_ok=True)
        fullPath = directory + "/" + fileName
        with open(fullPath, "w") as file:
            file.write("This is a file in the folder.")

    # list a directory element's.
    def listFiles():
        file = os.listdir()
        return print(file)
    
    # show you your current working directory. 
    def ProcessingDir():
        process = os.getcwd()
        return process

    # create folder and file method.
    def OsCreatefolder(name):
        if not os.path.exists(name):
            os.mkdir(name)
        return print('your directory %s' %name)

    # create folder and file method.
    def CreateFolders(path, name):
        if not os.path.exists(path):
             os.mkdir(path)
             os.makedirs(path +'/'+ name)
        return print('your directory %s' %path + name)
    
    # remove file method.
    def removeFile(name):
        os.remove(name)
        return print('your directory %s has  been removed.' %name)
    
    # remove Folder method.
    def cleanFolder(name):
        os.rmdir(name)
        return print('your directory %s has removed.' %name)
    
    # join Folder & file method.
    def join(parent, child, file):
        os.path.join(parent, child, file)
        return print('your directory %s and  is join with file ' %parent, child,file)