import os 
import shutil

from_dir = "C:/Users/User/Downloads/Downloads"

to_dir = "C:/Users/User/Documents/Document files"

listOfFiles= os.listdir(from_dir)

for fileName in listOfFiles:
    name,extension = os.path.splitext(fileName)
    if(extension ==''):
        continue

    if(extension in ['.gif', '.png', '.jfif', '.jpg']):
        path1 = from_dir+'/'+fileName
        path2 = to_dir+'/'+"Document_Files"
        path3 = to_dir+'/'+"Document_Files"+'/'+fileName

        if(os.path.exists(path2)):
            print('Moving '+fileName)
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print('Moving '+fileName)
            shutil.move(path1, path3)
            