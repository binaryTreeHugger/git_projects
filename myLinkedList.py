class Node:
  # constructor
  def __init__(self, data): 
    self.data = data
    self.next = None

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next


LL = LinkedList()

nodes = [1,2,3,4,5]
for i in nodes:
    LL.insert(i)
LL.printLL()

    
