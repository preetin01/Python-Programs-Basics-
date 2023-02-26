for i in range(int(input('enter the test cases: '))):
    a,b,x,y=map(int,input('enter the input: ').split())
    ax=(a/x)
    by=(b/y)
    print(ax,by)
    
    '''if ax==by:
        print('Both')
    elif ax>by:   
        print('Chef')
    elif ax<by:
        print('Chefina')'''