import os
import re

allFilesFolders=os.walk(r'C:\Users\Syed\Downloads\Python Session')
#reObj=re.compile(r'(.pdf)')

for (p,sf,fln) in allFilesFolders:
    for fl in fln:
        if '.txt' in fl:
            print(fl)
