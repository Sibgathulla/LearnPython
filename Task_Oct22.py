

def AcceptListOfValuesUntilExit():
    taskDescription='''Task to accept list of value till user enters exit
            '''
    print("\n\n\n",taskDescription,'\n')
    lsVals=[]
    while(True):
        val=input('Enter a value: ')
        if(val.lower()=='exit'):
            break
        lsVals.append(val)
    print(lsVals)

def AcceptUserNameAndAge():
    taskDescription='''Task to accept User Name & Age. And print in following format #
            [(age,User),(age,User),(age,User),(age,User)]
            '''
    print("\n\n\n",taskDescription,'\n')
    lsUser=[]
    lsAge=[]
    while(True):
        name=input('Enter User Name: ')
        if(name.lower()=='exit'):
            break
        age=int(input('Enter User age: '))
        
        lsUser.append(name)
        lsAge.append(age)
        
    lsUserNameAge=list(zip(lsUser,lsAge))
    print(lsUserNameAge)


def DictionaryWithForLoop():
    taskDescription='''Task to create a dictionary with one code statement (for loop)
            '''
    print("\n\n\n",taskDescription,'\n')
    dic=dict((int(input('Enter Key: ')),input('Enter Value: ')) for i in range(int(input('Enter range: '))))
    print(dic)

def main():
    DictionaryWithForLoop()
    AcceptListOfValuesUntilExit()
    AcceptUserNameAndAge()

main()
