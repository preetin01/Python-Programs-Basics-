class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        llist=''
        while itr:
            llist+=str(itr.data)+'-->'
            itr=itr.next                
        print(llist)    
if __name__ =='__main__':
    ll=LinkedList()
    #ll.insert_at_begining(10)
    #ll.insert_at_begining(5)   
    
    t=int(input("enter the number of nodes: "))
    for i in range(t):
        n=int(input("enter the nodes: "))
        ll.insert_at_begining(n)
    ll.print()     
    
    
     
   