from DoublyLinked import Deque
from DoublyLinked import Node


def wordToDeque(input):
    deque = Deque()#new list
    for char in input:#adds all characters to the new list
        deque.push(char)
    return deque

# Testing logic for wordToDeque, this code was provided
def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front is None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front != None:
        return False
    return True

# OffByOne function
def OffByOne(char1, char2):#this creates a new list then add the char to the list then stores the values to be compared in ascii
    deque = Deque()
    deque.push(char1)
    deque.push(char2)
    #Get the two characters from the deque
    first_char = deque.pop_front()
    second_char = deque.pop()
    return abs(ord(first_char) - ord(second_char)) == 1#converts it to ascii then takes the absolute value to see if they are off by 1 value

# OffByN function
def OffByN(char1, char2, N):#this creates a new list then add the char to the list then stores the values to be compared in ascii
    deque = Deque()
    deque.push(char1)
    deque.push(char2)
    #Get the two characters from the deque
    first_char = deque.pop_front()
    second_char = deque.pop()
    return abs(ord(first_char) - ord(second_char)) == N

#Testing OffByN
char1 = 'b'
char2 = 'e'
N = 3
print(OffByN(char1, char2, N)) #Should return True

#Testing OffByOne
char1 = 'b'
char2 = 'a'
print(OffByOne(char1, char2)) #Should return True

#Example test for wordToDeque
test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque)) #Should return True