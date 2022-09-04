#create node 
#create individual nodes

class Node: 
     def __init__(self,data) -> None:    #intialze the fields of node
          self.data = data     
          self.next = None            #  node1=Node(10)  data = 10 and refe is none

#node1=Node(10)  node has been created
#print(node1)
class Linkedlist:
    def __init__(self) -> None:
         self.head = None            #creating linked list is empty
 # performing traversal
    def printlinkedlist(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n=self.head      # if not empty,print data of that node
            while n is not None:
                print(n.data,"-->",end=" ")       #we use while loop cause we know only stooping condition, we dont know how many time we need to execute
                n=n.next
#LL1 = Linkedlist()
#LL1.printlinkedlist()"""
# insertion of elemnt at beginning
# create node 
#chnage reference of the node, new node will point frst node
# point head = new node
    def insertion_begin(self,data):
        new_node = Node(data)  # created node
        new_node.next = self.head  # changed the reference
        self.head = new_node  


    # insertion at the end of the linkedlist
    def insertion_end(self,data):
        new_node = Node(data)
        if self.head is None: #node is empty
            self.head= new_node
        else:
            n = self.head
            while n.next is not None: 
                n=n.next   # we are at last node
            n.next=new_node 
            new_node=None
    #insertion at the middle code same for adding after any node, except 1st node, we can add everywhere
    #make node,find x position,
    def insert_mid_after_node(self,data,x): # x= node after which we want to add new node 
        n=self.head
        while n is not None:
           if x==n.data:
              break
           n=n.next
        if n is None:
            print("node is not present")   
        else:    
            new_node=Node(data) 
            new_node.next=n.next # here x and n both are same
            n.next=new_node


LL1 = Linkedlist()
LL1.insertion_begin(3)
LL1.insertion_begin(70)
LL1.insertion_end(30)
LL1.insert_mid_after_node(5,30)
LL1.insertion_end(8)
LL1.printlinkedlist()        


     























