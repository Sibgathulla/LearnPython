"""
Requirement #

    Resolve Linear Equations


"""
import re

coefficientlhs=[]
coefficientrhs=[]

def IsValidEquations(equation):
    if "=" not in equation:
        return False
    
def ExtractCoefficient(equation):
    reObj=re.compile(r'-?\d+')
    coefficient=reObj.findall(equation)
    return coefficient
    #print(coefficient)
    
def ExtractLHS(coefent):
    #print(coefent)
    lhs=[]
    for i in range(len(coefent)-1):
        #print('\n',i,len(coefent)-1)
        lhs.append(int(coefent[i]))
    #print(lhs)
    return lhs

def ExtractRHS(coefent):
    rhs=[]
    rhs.append((int(coefent[len(coefent)-1])))
    #print(rhs)
    return rhs

def AcceptLinearEquation(i):
    equation=input('Provide Linear equation: ')
    if(IsValidEquations(equation)==False):
        print('Invalid equation')
        return
    
    coefent = ExtractCoefficient(equation)

    lhs= ExtractLHS(coefent)
    rhs= ExtractRHS(coefent)
    
    #print(lhs)
    #print(rhs)
    
    coefficientlhs.append(lhs)
    coefficientrhs.append(rhs)

def main():
    numberOfEquations=int(input('Number of linear equations to resolve: '))
    for i in range(numberOfEquations):
        AcceptLinearEquation(i)

    print(coefficientlhs)
    print(coefficientrhs)

main()
