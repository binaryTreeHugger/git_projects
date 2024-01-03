#################################################
##          Is Binary Tree Sorted?             ##  
#################################################

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

        
def isSorted(root, minVal=float('-inf'), maxVal=float('inf')):
    if root is None:
        return True

    if minVal < root.data < maxVal:
        leftSorted = isSorted(root.left, minVal, root.data)
        rightSorted = isSorted(root.right, root.data, maxVal)
        return leftSorted and rightSorted
    else:
        return False

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(8)


#################################################
##                  Binary Search              ##  
#################################################

def binarySearch(array, x):
    left = 0; right = len(array)-1
    while left <= right:
        middle = (left + right)//2
        if array[middle] == x:
            return middle
        if array[middle] > x:
            right = middle - 1
        if array[middle] < x:
            left = middle + 1
    print("Not Found")
    return -1

#################################################
##        Recursive Binary Search              ##  
#################################################

def recBinSearch(array, x, left, right):
    if left <= right:
        middle = (left + right)//2
        if array[middle] == x:
            return middle
        if array[middle] > x:
            right = middle - 1
            return recBinSearch(array,x,left, right)
        if array[middle] < x:
            left = middle + 1
            return recBinSearch(array,x,left, right)
    else:
        print("Not Found")
        return -1

#################################################
##                  Merge                      ##  
#################################################

def merge(left, right):
    i, j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result

#################################################
##                  Merge Sort                 ##  
#################################################

def mergeSort(array):
    if len(array) <= 1:
        return array
    middle = len(array)//2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return merge(left, right) 

#################################################
##                 Bubble Sort                 ##  
#################################################

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i],array[j] = array[j],array[i]
    return array

#################################################
##              Selection Sort                 ##  
#################################################

def selectionSort(array):
    for i in range(len(array)):
        i_min = i
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                i_min = j
        array[i],array[i_min] = array[i_min],array[i]
    return array

#################################################
##             Returning Change                ##  
#################################################

def giveChange(change):
    coins = {'quarter':25, 'dime':10, 'nickel':5, 'penny':1}
    q = change//coins['quarter']
    change = change % coins['quarter']
    
    d = change//coins['dime']
    change = change % coins['dime']

    n = change//coins['nickel']
    change = change % coins['nickel']

    p = change
    return (q,d,n,p), (q+d+n+p)

#################################################
##       Longest Increasing Sequence           ##  
#################################################
        
def lis(arr):
    t = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                t[j] += 1
    return max(t)

#################################################
##             Depth First Search              ##  
#################################################

foo = {'a' : set(['b','c']),
       'b' : set(['a','d','e']),
       'c' : set(['a','f','g']),
       'd' : set(['b','h','i']),
       'e' : set(['b','j','k']),
       'f' : set(['c','l','m']),
       'g' : set(['c','n','o']),
       'h' : set(['d']),
       'i' : set(['d']),
       'j' : set(['e']),
       'k' : set(['e']),
       'l' : set(['f']),
       'm' : set(['f']),
       'n' : set(['g']),
       'o' : set(['g'])}

bar = {'a' : ['b','c'],'b': ['a'], 'c' : ['a']}

def dfs(graph,start):
    explored = set()
    frontier = [start]
    while frontier:
        node = frontier.pop()
        if node not in explored:
            explored.add(node)
            print(node)
            frontier.extend(graph[node] - explored)
    return


#################################################
##             Breadth First Search            ##  
#################################################

def bfs(graph,start):
    explored = set()
    frontier = [start]
    while frontier:
        node = frontier.pop(0)
        if node not in explored:
            explored.add(node)
            print(node)
            frontier.extend(graph[node] - explored)
    return

#################################################
##                Anagram Verifier             ##  
#################################################

def isAnagram(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    alphCount1 = [0 for i in range(26)]
    alphCount2 = [0 for i in range(26)]
    for letter in word1:
        alphCount1[ord(letter) - ord('a')] += 1
    for letter in word2:
        alphCount2[ord(letter) - ord('a')] += 1
    return alphCount1 == alphCount2

#################################################
##             Palindrome Verifier             ##  
#################################################

def isPalindrome(string):
    middle = len(string) // 2
    end = len(string) -1
    if len(string) <= 1:
        return True
    for i in range(middle):
        print('comparing ', string[i], ' and ', string[end -i])
        if string[i] != string[end - i]:
            return False
    return True

#################################################
##             Make String Lowercase           ##  
#################################################

def lower(string):
    result = ''
    low = ord('A'); high = ord('Z'); diff = ord('a') - ord('A')
    for letter in string:
        if ord(letter) >= low and ord(letter) <= high:
            lowerCase = chr(ord(letter) + diff)
            result += lowerCase
        else:
            result += letter
    return result

#################################################
##             Make String Upperercase         ##  
#################################################

def upper(string):
    result = ''
    low = ord('a'); high = ord('z'); diff = ord('a') - ord('A')
    for letter in string:
        if ord(letter) >= low and ord(letter) <= high:
            upperCase = chr(ord(letter) - diff)
            result += upperCase
        else:
            result += letter
    return result

#################################################
##                  Print Hangman              ##  
#################################################

person = ['O', '|', '/', '\\', '/', '\\']
def printHangman():
    print("_____")
    print("|/  |")
    print("|   {}".format(person[0]))
    print("|  {}{}{}".format(person[2],person[1],person[3]))
    print("|  {} {}".format(person[4],person[5]))
    print("|")
    print("oooooooo")


#################################################
##                  Sum Pair                   ##  
#################################################


def sumPair(array, x):
    compList = {}
    for i in range(len(array)):
        comp = x - array[i]
        if array[i] in compList:
            return compList[array[i]],i
        else:
            compList[comp] = i
    print("Not found")
