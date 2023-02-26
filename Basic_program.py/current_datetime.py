import datetime
now=datetime.datetime.now()
print("THE CURRENT DATETIME IS: ",end='')
print(now.strftime('%y-%m-%d : %H-%M-%S'))