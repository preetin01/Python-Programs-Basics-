print('Welcome to Iron Bank of Bravoos ATM')
restart=('Y')
chances=3
balance=67.14
while chances>=0:
    pin=int(input('Please Enter You4Digit Pin:'))
    if pin==(1234):
        print('You entered your pin Correctly\n')
        while restart not in('n','NO','no','N'):
            print('Please Press1For Your Balance\n')
            print('Please Press2To MakeaWithdrawl\n')
            print('Please Press3To Pay in\n')
            print('Please Press4To Return Card\n')
            option=int(input('What Would you like to choose?'))
            if option ==1:
                print('Your Balance isÂ£',balance,'\n')
                restart=input('Would You you like to go back?')
                if restart in('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option ==2:
                option2=('y')
                withdrawl=float(input('How Much Would you like to withdraw?\nÂ£10/Â£20/Â£40/Â£60/AE80/AE100 for other enter 1:'))
                if withdrawl in [10,20,40,60,80,100]:
                    print('\nYour Balance is nowÃ£',(balance-withdrawl))
                    restart=input('Would You you like to go back?')
                    if restart in('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl!=[10,20,40,60,80,100]:
                    print('Invalid Amount,Please Re-try\n')
                    restart=('y')
                elif withdrawl ==1:
                    withdrawl =float(input('Please Enter Desired amount:'))
            elif option ==3:
                Pay_in=float(input('How Much Would You Like To Pay In?'))
                balance=balance+Pay_in
                print('\nYour Balance is nowÂ£',balance)
                restart=input('Would You you like to go back?')
                if restart in('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option ==4:
                print("Please wait whilst your card is Returned ...\n")
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number.\n')
                restart=('y')
    elif pin!=('1234'):
        print('Incorrect Password')
        chances=chances-1
        if chances ==0:
            print("\nNo more tries")
            break