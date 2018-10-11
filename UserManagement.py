"""
User Management #

1. Create user
    Ask - First Name, Last Name,
          User Name - No same user name
          Password - Should be alpha numaric,
                     Should have a Capital letter,
                     Should have a number
2. Login User
    Should allow only creted users to login
    Successful login print - Welcome Fist + Last name

"""

#Start DB variables

DicUser={"MasterAdmin":1000} #Key=UserName, Value="UserId"
DicUserPassword={1000:"M@$t3r1"}
DicUserDetails={1000:"Master,Admin"}

#End DB variables

#Start DB related functions

def GetLastValue(DicUser):
    #Not working function
    values=set(DicUser.values())
    print(values)
    lastVal=values.pop()
    print(lastValue)
    return lastValue

def GetCurrentUserId():
    #return GetLastValue(DicUser)
    values=set(DicUser.values())
    return max(values)

def ExsistingUser(userName):
    return not DicUser.get(userName)== None

def PersistUserInfo(firstName,lastName,userName,password):
    currentUserId=GetCurrentUserId()
    currentUserId=currentUserId+1

    DicUser[userName]=currentUserId
    DicUserPassword[currentUserId]=password

    name=firstName+','+lastName
    DicUserDetails[currentUserId]=name
    
    #print(DicUser)
    #print(DicUserDetails)
    #print(DicUserPassword)
    return True


def GetAllUsers():
    allUsers='\n\nUser Name'.rjust(15,' ')+'First Name'.rjust(15,' ')+'Last Name'.rjust(15,' ')
    allUsers=allUsers+'\n'+'='*50
    #print('\n\nUser Name'.rjust(15,' '),'First Name'.rjust(15,' '),'Last Name'.rjust(15,' '))
    #print('='*50)
    for i in DicUser:
        name=DicUserDetails.get(DicUser[i]).split(',')
        firstName=name[0]
        lastName=name[1]
        allUsers=allUsers+'\n'+i.ljust(15,' ')+firstName.ljust(15,' ')+lastName.ljust(15,' ')
        #print(i.ljust(15,' '),firstName.ljust(15,' '),lastName.ljust(15,' '))

    return allUsers


#End DB related functions


#Start Validation function


def IsValidProperty(propName,propValue):
    if propName=='FirstName' or propName=='LastName' or propName=='UserName':
        return propValue.isalnum()
    elif propName=='Password':
        return len(password)>5 and password.isalnum() and password==confirmPassword
        


#End Validation function

def CaptureOperations():
    print('\n'*4)
    print('1. {0}\n2. {1}\n3. {2}\n4. {3}'.format('Login','Create User','List of users','Exit'))
    operation=int(input('Provide an option: '))
    return operation


def DisplayAllUsers():
    print(GetAllUsers())


def CreateUser():
    print('\n\n\n Please provide following fields. * is mandatory')
    while(True):
        firstName=input('*First Name: ')
        if(not firstName.isalnum()):
            print('Please provide valid first name')
        else:
            break;
        
    while(True):
        lastName=input('*Last Name: ')
        if(not lastName.isalnum()):
            print('Please provide valid last name')
        else:
            break;
        
    while(True):
        userName=input('*User Name: ')
        if(not userName.isalnum()):
            print('Invalid UserName.')
        elif(ExsistingUser(userName)):
            print('User already exsist. Please select another user.')
        else:
            break;
            
    while(True):
        password=input('*Password: ')
        confirmPassword=input('Confirm Password: ')
        if len(password)>5 and password.isalnum() and password==confirmPassword:
            break;
        print('Please enter valid password.')

    if(PersistUserInfo(firstName,lastName,userName,password)):
        print(userName,' created successfully.')
    else:
        print('Sorry, unable to create user.')

    


while(True):
    operation = CaptureOperations()
    if(operation==1):
        print('Login is not yet implemented')
        #UserLogin()
    elif(operation==2):
        CreateUser()
    elif(operation==3):
        DisplayAllUsers()
    elif(operation==4):
        print('\n\nGood Bye!')
        break
