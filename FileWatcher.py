'''
FileWatcher for file updates.

'''

import os
import platform
import time

def FileWatcher():
    previousUpdate=0
    count=0
    try:
        while(True):
            lastUpdate = FileLastUpdate('Sample.txt')
            #print(previousUpdate,lastUpdate)
            if(previousUpdate<lastUpdate):
                print('File got updates at ',lastUpdate)
                count=count+1
            time.sleep(5) # sleep for 5 seconds
            previousUpdate=lastUpdate
    except KeyboardInterrupt:
        print('Terminating the program !!!')
        return

def FileLastUpdate(filePath):
    if platform.system() == 'Windows':
        return os.path.getmtime(filePath)
    else:
        #For MAC
        stat = os.stat(filePath)
        try:
            return stat.st_birthtime
        except AttributeError:
            # For Linux
            return stat.st_mtime

def main():
    FileWatcher()

main()
