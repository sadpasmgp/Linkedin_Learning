class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):

        """
        Accepts an item as a parameter 
        and appends it to the end of the list

        The runtime for this method is O(1) or constant time, 
        because appending to the end of a list happens in a constant time.
        """
        
        self.items.append(item)

    def pop(self):

        """
        Removes and returns the last item for the list.
        The runtime for this method is O(1) or constant time,
        """

        if self.items:
            return self.items.pop()
        return "Empty stack"

    def peek(self):

        """
        Returns the last item in the list, lso the item at top of list.
        The runtime for this method is O(1) or constant time
        because indexing is done in constant time.
        """

        if self.items:
            return  self.items[-1]
        return "Empty stack. No items to peek at"

    def size(self):

        """
        This method returns the length of the list
        that is represting the stack.

        This method runs in constant time because finding
        length of list also happens in constant time
        """

        if self.items:
            return len(self.items)
        return "size is 0 as stack is empty"

    def is_empty(self):

        """
        This method checks if the list is empty
        by looking at the size of the stack.

        This method runs in constant time because finding
        length of list also happens in constant time.
        """

        if len(self.items) == 0:
            return "stack is empty"
        elif len(self.items)>0:
            return "stack is not empty"
        else:
            return "Unknown stack size.cannot be determined"