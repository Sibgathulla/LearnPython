import os
"""
Requirement #

Write data to file in a specific format, so that it can be read properly.

Lets have following format -

User -> TableName
====================
Id,UserName ->Table columns
====================
1000,MasterAdmin -> Table Data/rows 
1001,Admin


"""

def CreateTable(tableName,columns):
    fileObj=open('DbFile.txt',w)
    fileObj.writeline(tableName)
    fileObj.writeline('='*20)
    for column in 
    
