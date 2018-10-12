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

def IsExists(tableName):
    fileExtension='txt'
    fileName=tableName+'.'+fileExtension
    return os.path.exists(fileName)

def CreateTable(tableName,columns):
    fileExtension='txt'
    fileName=tableName+'.'+fileExtension
    if(tableName!='' and not os.path.exists(fileName)):
        fileObj=open('DbFile.txt','w')
        #fileObj.write(tableName+'\n')
        print('File created and ready to write..')
        #fileObj.writeline('='*20)
    else:
        fileObj=open(fileName,'a')
        print('File is ready for appened..');
    rowColumn=''
    for column in columns:
        if rowColumn != '':
            rowColumn=rowColumn+','
        rowColumn=rowColumn+column
    fileObj.write(rowColumn)

    fileObj.close()

    return true

def GetAllColumns(tableName):
    fileObj=open('DbFile.txt','r')
    columns = fileObj.readline()
    lsColumns=colums.spilt(',')
    return lsColumns

def CheckAndCreateSchema(tableName):
    if(tableName==''):
        print('Invalid table name..!')
        return
    if(not IsExists(tableName)):
        columns=[]
        print('Please provide columns, enter 0000 when done..!') 
        while(True):
            columnName=input('Column Name: ')
            if(columnName=='0000')
                break;
            columns.append(columnName)
            
        CreateTable(tableName,columns)
    else:
        print('Please provide data for table: ',tableName)
        columns=GetAllColumns(tableName)
        columnVal=[]
        for column in columns:
            val=input(column+': ')
            columnVal.append(val)
        if(CreateTable(tableName,columns)):
            print('Data added successfully..!')
                
            
        
        
    
def main():
    tableName=input('Enter table Name: ')
    CheckAndCreateSchema(tableName)

main()
