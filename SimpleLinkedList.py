class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def display(self):
        nodes = []
        current = self.head
        while current.next:
            current = current.next
            nodes.append(current.data)
        print(nodes)

    def length(self):
        count = 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def get(self, index):
        if index >= self.length():
            print("Error: Out of range")
            return None
        currentNode = self.head
        current_i = 0
        while True:
            currentNode = currentNode.next
            if current_i == index:
                return currentNode.data
            current_i += 1

    def erase(self, index):
        if index >= self.length():
            print("Error: Out of range")
            return None
        currentNode = self.head
        current_i = 0
        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if current_i == index:
                lastNode.next = currentNode.next
                return
            current_i += 1

myList = LinkedList()
for i in [1,3,5,7]:
    myList.append(i)

myList.display()
myList.erase(0)
myList.display()
