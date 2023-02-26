def TomJerry(n):

    if n%3==0 and n%5==0:
        print('TOMJERRY')
    elif n%3==0:
        print('TOM')
    elif n%5==0:
        print('JERRY')
    else:
        print('NOT DIVISIBLE') 
           
n=int(input('Enter the number:'))
TomJerry(n)        
               