
"""List if primes numbers

ListOfPrimeNumber vs ListOfPrimeNumberUsingThread
Performance # ListOfPrimeNumber
Note# Might need to work on threads to bring ListOfPrimeNumberUsingThread
    
Following are performance of ListOfPrimeNumber

Provide range: 100000
Time taken to find prime:  29.828161001205444  Sec

Provide range: 1000000
Time taken to find prime:  2641.140676498413  Sec

"""
import time
import threading

def IsPrime(nmbr):
    if(nmbr%2==0):
        return False
    hlfNmbr=nmbr//2
    for cuntr in range(3,hlfNmbr,2):
        if nmbr%cuntr==0:
            return False
    return True

def ListOfPrimeNumberUsingThread(rnge): 
    startTime=time.time()
    for cuntr in range(1,rnge+1):
        t = threading.Thread(target=IsPrime, args=(cuntr,))
        t.daemon = True
        t.start()
        #t.join()
    print('Time taken to find prime: ',time.time()-startTime,' Sec')
    #print(lsPrime)


def ListOfPrimeNumber(rnge):
    #lsPrime=[]
    startTime=time.time()
    for cuntr in range(1,rnge+1):
        IsPrime(cuntr)
        #if(IsPrime(cuntr)):
            #lsPrime.append(cuntr)
    print('Time taken to find prime: ',time.time()-startTime,' Sec')
    #print(lsPrime)



def Main():
    print('List of prime numbers between 1 and provided range...')
    rnge=0
    while(rnge<=0):
        rnge=int(input('Provide range: '))
    ListOfPrimeNumber(rnge)

    
Main()
