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
        fileObj=open(fileName,'w')
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
    fileObj.write(rowColumn+'\n')

    fileObj.close()

    return True

def GetAllColumns(tableName):
    fileExtension='txt'
    fileName=tableName+'.'+fileExtension
    fileObj=open(fileName,'r')
    columns = fileObj.readline()
    lsColumns=columns.split(',')
    return lsColumns

def CheckAndCreateSchema(tableName):
    if(tableName==''):
        print('Invalid table name..!')
        return
    if(not IsExists(tableName)):
        columns=[]
        print('Please provide columns, enter 0x0x0 when done..!') 
        while(True):
            columnName=input('Column Name: ')
            if(columnName=='0x0x0'):
                break;
            columns.append(columnName)
            
        CreateTable(tableName,columns)
    else:
        print('Please provide data for table: ',tableName)
        columns=GetAllColumns(tableName)
        columnVal=[]
        for column in columns:
            val=input(column.strip()+': ')
            columnVal.append(val)
        if(CreateTable(tableName,columnVal)):
            print('Data added successfully..!')
                
            
def DisplayAllUsers(tableName):
    fileExtension='txt'
    fileName=tableName+'.'+fileExtension
    fileObj=open(fileName,'r')
    isheader=True
    allUsers=''
    for columnsRow in fileObj:
        if isheader:
            allColumns=columnsRow.split(',')
            for column in allColumns:
                allUsers = allUsers + column.rjust(5+len(column),' ')
            allUsers=allUsers+'\n'+'='*50
            isheader=False
        else:
            allColumns=columnsRow.strip().split(',')
            allUsers=allUsers+'\n'
            for column in allColumns:
                allUsers = allUsers + column.ljust(10,' ')
                #allUsers=allUsers+'\n'+'='*50
            
    print(allUsers)
    fileObj.close()
    
def main():
    tableName=input('Enter table Name: ')
    CheckAndCreateSchema(tableName)
    DisplayAllUsers(tableName)

main()
