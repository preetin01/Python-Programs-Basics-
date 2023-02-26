class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        
    #def insert_at_begining(self,data):
     #   node=Node(data,self.head)
      #  self.head=node
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
        
    def insert_at_end(self,data): 
        if self.head is None:
            self.head=Node(data,None) 
            self.head=Node(data,None)
            return
        itr =self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
             
          
if __name__ =='__main__':
    ll=LinkedList()
    
    #ll.insert_at_begining(5)
    #ll.insert_at_begining(10) 
    #ll.insert_at_end(15)
    #ll.insert_at_end(20)   
    #ll.print()
    
    t=int(input("enter the number of nodes: "))
    for i in range(t):
        n=int(input("enter the node: "))
        ll.insert_at_end(n)
    ll.print()    