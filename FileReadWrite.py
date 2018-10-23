import os
import csv
import re

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
                #allUsers=allUser+'\n'+'='*50
            
    print(allUsers)
    fileObj.close()

def DisplayAllUsersUsingCVS(tableName,deleteData):
    fileExtension='txt'
    fileName=tableName+'.'+fileExtension
    with open(fileName) as fp:
        csvreader = csv.DictReader(fp)
        columns=csvreader.fieldnames
        print(columns[0].rjust(5+len(columns[0]),' '),columns[1].rjust(5+len(columns[1])))
        for row in csvreader:
            print(row[columns[0]].ljust(15,' '),row[columns[1]].ljust(15,' '))



            
def DeleteToDo():
    print ("Which Item Do You Want To Delete?")
    DeleteItem = raw_input(">") #select a line number to delete
    print ("Are You Sure You Want To Delete Number" + DeleteItem + "(y/n)")
    DeleteItem=int(DeleteItem) 
    VerifyDelete = str.lower(raw_input(">"))
    if VerifyDelete == "y":
        FILE = open('data.txt',"r") #open the file (tried w+ as well, entire file is deleted)
        lines=[x.strip() for x in FILE if int(x[:x.index('.')])!=DeleteItem] #read all the lines first except the line which matches the line number to be deleted
        FILE.close()
        FILE = open('data.txt',"w")#open the file again
        for x in lines:FILE.write(x+'\n')    #write the data to the file
    else:
        print ("Nothing Deleted")


def SearchFileUsingRegEx(tableName):
    dataToSearch=input('Provide data to search: ')
    #result=[re.findall(r'f\(\s*([^,]+)\s*,\s*([^,]+)\s*\)',line) 
    #       for line in open('Sample.txt')]
    #print(result)
    #regex = re.compile("f\(\s*([^,]+)\s*,\s*([^,]+)\s*\)")
    regex = re.compile(r"1000\w*[^,]*")
    #regex=re.compile(r'1000\w^\s*[^#]*IgnoreRhosts\s')
    with open("User.txt") as f:
        for line in f:
            result = regex.search(line)
            if(result!=None):
                print(result)
                


        
def main():
    tableName=input('Enter table Name: ')
    #CheckAndCreateSchema(tableName)
    #DisplayAllUsers(tableName)
    #DisplayAllUsersUsingCVS(tableName,'')
    SearchFileUsingRegEx(tableName)

main()
