"""
TASk ###
    Program to handle exception using Try Except
    Iterate through list of integers and divide input number with list number
    if zero found as part of the list prompt for input for that list index element.
"""

def WithoutSort():
    a=int(input('enter a value: '))
    b=[1,2,0,4]
    i=0
    while(i<len(b)):
        try:
            c=a/b[i]
            print(c)
            i=i+1
        except ZeroDivisionError:
            b[i]=int(input(str(b[i])+' is invalid. Please provide value: '))
        except IndexError:
                print('Index out of bound')

def WithSort():
    a=int(input('enter a value: '))
    b=[1,2,0,4]
    b.sort()
    print(b)
    while True:
        for i in range(len(b)):
            try:
                c=a/b[i]
                print(c)
            except ZeroDivisionError:
                b[i]=int(input(str(b[i])+' is invalid. Please provide value: '))
                break
            except IndexError:
                print('Index out of bound')
        if(i==len(b)-1):
            break


def main():
    WithSort()
    WithoutSort()

main()
