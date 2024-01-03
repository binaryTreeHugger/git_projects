class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    def getLength(self):
        count=0
        current = self.head
        while current.next is not None:
            count +=1
            current = current.next
        return count
    def display(self):
        nodes = []
        current = self.head
        while current.next:
            current = current.next
            nodes.append(current.data)
        print('->'.join([str(i) for i in nodes]))
        
    def goTo(self,index):
        if index >= self.getLength():
            print("Error: Out of bounds"); return
        current = self.head
        i = 0
        while current.next is not None:
            current = current.next
            if index == i:
                return current.data
            i += 1
    def remove(self,n):
        count = 0
        current = self.head
        while current.next is not None:
            prev = current
            current = current.next
            if count == n:
                prev.next = current.next
            count += 1
    def replace(self,n,rep):
        count = 0
        current = self.head
        while current.next is not None:
            current = current.next
            if count == n:
                current.data = rep
                return rep
            count += 1

fooList = LinkedList()
for i in [i for i in range(100) if i%2 == 0]:
    fooList.insert(i)

fooList.display()
