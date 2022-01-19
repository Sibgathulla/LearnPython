import hashlib

def GetChar(idx):
       return chr(idx)

def StringToHash256(input):
    result = hashlib.sha256(input.encode())
    return result.hexdigest()

def GenerateData(len):
    print('GenerateData of length.. '+str(len))

    indx=1
    while(indx<=len):    
        for i in range(97,97+26):
            j=1
            result=''
            while(j<=indx):
                result=result+GetChar(i)
                j=j+1
            print(result)
        indx=indx+1
    
def GenerateDataRec(position):
    result=GetChar(position)
    print(result)
    if(position<97+26-1):
        return GenerateDataRec(position+1)

def main():
    print('this is test application..')
    # for i in range(97,97+5):
    #     input1=GetChar(i)
    #     for idx in range(97, 97 + 26):
    #         input=GetChar(idx)
    #         print(input1+input)
    #         output=StringToHash256(input)
    #         print(input + '  '+output)
    # i=1
    # while(i<=10):
    #     print(i)
    #     i=i+1
    # i=1 
    # len=3
    # while(i<=len):
    #     GenerateData(i)
    #     i=i+1
    # GenerateData(3)
    GenerateDataRec(97)
main()