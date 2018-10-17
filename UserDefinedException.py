"""
TASK#

Calculate area of rectangle
    when length<=0 or breadth <=0, prompt user to enter the value again.

"""

def Area(length,breadth):
    if length==0:
        raise Exception('Invalid Length')
    if(breadth==0):
        raise Exception('Invalid Breadth')

    area=length*breadth
    print('Area of rectangle is ',area)

def main():
    length=float(input('Provide Length: '))
    breadth=float(input('Provide Breadth: '))
    while(True):
        try:
            Area(length,breadth)
            break
        except Exception as ex:
            if 'Length' in str(ex):
                length=float(input('Invalid Length, Provide Length: '))
            if 'Breadth' in str(ex):
                breadth=float(input('Invalid Breadth, Provide Breadth: '))
            
    

main()
