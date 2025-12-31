
import numpy as np

class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = -1
        self.back = -1
        self.size = 0
        self.array = np.zeros(self.capacity, dtype=object)
    def empty(self):#same as doubly
        """Check whether the deque is empty."""
        return self.size == 0

    def get_size(self) -> int:#same as doubly
        """Return total number of elements in deque."""
        return self.size

    def push_front(self, data):
        """Push an element to the front of the deque."""

        if self.size == self.capacity:#checks to make sure there is room in the list
            self.resize()
        if self.empty():
            self.front = self.back = 0#sets the index at 0 and then gets ready to add
        else:
            if self.front == 0:
                self.front = self.capacity - 1#goes to last item in array
            else:
                self.front -= 1#ressets index

        self.array[self.front] = data#adds to the front
        self.size += 1

    def push(self, data):#same as push front but for the back
        """Push an element at the back of the deque."""
        if self.size == self.capacity:
            self.resize()
        else:
            if self.back == 0:#starts at 0
                self.back = self.capacity - 1#goes to first item in array
            else:
                self.back += 1#ressets index

        self.array[self.back] = data#adds to the back
        self.size += 1

    def pop_front(self):
        """Pop an element from the front of the deque."""
        if self.empty():
            raise IndexError("This is an empty array")
        value = self.array[self.front]
        self.array[self.front] = None #Clears the front spot so we can add a pop
        if self.front == self.capacity - 1:
            self.front = 0 #Wraps around to the start
        else:
            self.front += 1 #Moves front index forward
        self.size -= 1
        return value

    def pop(self):
        """Pop an element from the back of the deque."""
        if self.empty():
            raise IndexError("This is an empty array")
        value = self.array[self.back]
        self.array[self.back] = None #Clears a spot in back to add a new pop
        if self.back == 0:
            self.back = self.capacity - 1 #Wraps around to the last item
        else:
            self.back -= 1 #Moves back index back
        self.size -= 1
        return value

    def resize(self):
        """Resize the deque to double its capacity."""
        new_capacity = self.capacity * 2
        new_array = np.zeros(new_capacity, dtype=object)

        for i in range(self.size):
            index = (self.front + i)
            if index >= self.capacity:
                index -= self.capacity#Wrap around to the start
            new_array[i] = self.array[index]

        self.array = new_array
        self.front = 0
        if self.size > 0:
            self.back = self.size - 1 #Set back to the last valid element in the new array
        else:
            self.back = 0 #Handle the case when there are no elements
        self.capacity = new_capacity
