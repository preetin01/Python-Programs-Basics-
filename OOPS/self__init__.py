class employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        
    def printdetail(self):
        return f"The name is(self.name).salary is(self.salary) and role is(self.role)"   
harry=employee('HARRY',500,'STUDENT')  
print(harry.name)      
print(harry.__dict__)