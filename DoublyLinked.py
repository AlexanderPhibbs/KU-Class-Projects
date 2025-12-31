


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def empty(self):
        """Check whether the deque is empty."""
        return self.size == 0#true if true else false

    def get_size(self) -> int:
        """Return total number of elements in deque."""
        return self.size#returns size as an int

    def push_front(self, data):
        """Push an element to the front of the deque."""
        new_node = Node(data)#creates a new node putting the item in there
        if self.empty():#checks to see if its empty already and returns true/false
            self.front = self.back = new_node#if empty then it sets the new node as the first and last node
        else:
            new_node.next = self.front#adds to front
            self.front.prev = new_node#changes the prev pointer to the new node which will be the current node
            self.front = new_node #makes sure the front pointer is on the node i just added
        self.size += 1#added to size

    def push(self, data):
        """Push an element at the back of the deque."""
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            new_node.prev = self.back#adds to back
            self.back.next = new_node#changes the pointer to the correct node from the back position
            self.back = new_node#sets the current pointer on the back node that we just added
        self.size += 1

    def pop_front(self) -> int:
        """Pop an element from the front of the deque."""
        if self.empty():
            raise IndexError("This is an empty list")#tells the user if its empty and fails the pop
        value = self.front.item#gets the number thats at the front of the list to "pop" off
        self.front = self.front.next#moving the pointer
        if self.front:
            self.front.prev = None#removes pointer from node we are getting rid of
        else:
            self.back = None#Deque is now empty
        self.size -= 1#removes on from size
        return value

    def pop(self) -> int:#exact same as the previous function but popping the back of the list instead
        """Pop an element from the back of the deque."""
        if self.empty():
            raise IndexError("This is an empty list")
        value = self.back.item
        self.back = self.back.prev
        if self.back:
            self.back.next = None
        else:
            self.front = None
        self.size -= 1
        return value

    def get_front(self) -> int:
        """Access first element of deque."""
        if self.empty():
            raise IndexError("This is an empty list")#raises and error if the list is empty
        return self.front.item#returns the item in the first node of the list

    def get_back(self) -> int:
        """Access last element of deque."""
        if self.empty():
            raise IndexError("This is an empty list")#raises and error if the list is empty
        return self.back.item#returns the item in the last node of the list

def is_palindrome(s: str) -> bool:
    deque = Deque()
    for char in s:
        deque.push(char)#Pushes all characters into the list
    while not deque.empty():
        front_char = deque.pop_front()#pops the front character off front and back and compares them
        back_char = None
        if not deque.empty():
            back_char = deque.pop()#does the same from back
        if back_char is not None and front_char != back_char:#checks to see if they are not the same
            return False
    return True

# Function to reverse a deque
def reverse_deque(deque):
    reversed_deque = Deque()
    # Iterate through the deque and add items to reversed_deque
    while not deque.empty():#single loop to remove from back and add the the front preserving the list integrity
        reversed_deque.push(deque.pop())
    return reversed_deque#return new list that is reversed


deque = Deque()
deque.push(1)
deque.push(2)
deque.push(3)

reversed_deque = reverse_deque(deque)
while not reversed_deque.empty():
    print(reversed_deque.pop_front())  # Should output 3, 2, 1.