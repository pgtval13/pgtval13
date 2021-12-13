class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self,index):
        if index >= self.size or index < 0:
            return -1
        cur_node=self.head #initialize    
        for x in range(index):
            cur_node=cur_node.next #traverse through the linked list
        return cur_node.data
    
    def appendAtIndex(self,index,data):
        if index > self.size or index<0:
            return 
        cur_node=self.head #initialize
        new_node=node(data)
        if index == 0: #for adding to Head(index zero)
            new_node.next=cur_node
            self.head=new_node
        else:           
            for x in range(index-1):
                cur_node=cur_node.next #traverse through the linked list
            new_node.next=cur_node.next #access next attribute(object) of current node and store it as next attribute(object) of new_node
            cur_node.next=new_node #add new node object as next attribute(object) of current node
        self.size += 1      

    def appendAtTail(self,data):
        self.appendAtIndex(self.size,data)

    def appendAtHead(self,data): 
        self.appendAtIndex(0,data)
   
    def deleteAtIndex(self,index):
        if index >= self.size or index < 0:
            return
        cur_node=self.head #initialize 
        if index==0:
            self.head=self.head.next
        else:
            for x in range(index-1):
                cur_node=cur_node.next #traverse through the linked list
            #skip a node because we are getting rid of that node
            #access the node after the next node and store it in cur_node
            cur_node.next=cur_node.next.next
            #below is an equivalent of above code
            #cur_node_next=cur_node.next
            #cur_node.next=cur_node_next.next
        #reduce the size because a node was removed
        self.size -= 1
        
    def length(self):
        return self.size

    def display(self):
        elements = []
        cur_node = self.head    #initialize
        for x in range(self.size):  
            elements.append(cur_node.data) #insert in elements data of current node
            cur_node=cur_node.next #traverse through the linked list
        return elements

sample_list = linked_list()

#append at index 0 
#sample_list.appendAtIndex(0,1)
#sample_list.display()

#create a linked list and create node on index 1 without node on index 0
#sample_list.appendAtIndex(1,0)
#sample_list.display()
#print(sample_list.get(0))

sample_list.appendAtTail('a')
sample_list.appendAtTail('c')
sample_list.appendAtTail('d')
sample_list.appendAtTail('f')

print(sample_list.display())
print(sample_list.get(2))
sample_list.deleteAtIndex(2)
print(sample_list.get(2))
sample_list.appendAtIndex(3,'apple')
print(sample_list.get(3))
#print(sample_list.display())

sample_list.appendAtIndex(0,'orange')
print(sample_list.display())
print("length is %d" % sample_list.length())