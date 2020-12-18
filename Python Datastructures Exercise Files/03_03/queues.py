class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Takes in an item and 
        inserts that itm into the 0th index of the list
        that is representing the Queue

        The runtime is O(n) or linear time, 
        because inserting into the 0th index of a list 
        forces all the other items in the list to move 
        one index to the right
        """
        self.items.insert(0, item)


    def dequeue(self):
        """
        Returns and removes front-most item of the Queue, 
        which is represented by the last item in the list.

        The runtime is O(1) or constant time, 
        because insexing to the end of list happens in constant time
        """
        if self.items:
            return self.items.pop()
        return f"Queue is empty"

        
    def peek(self):
        """
        Returns last item in the list , which represents the front-most
        item in the Queue.

        The runtime is constant because we're just
        indexing to the last item of the list
        and returning the value found there
        """

        if self.items:
            return self.items[-1]
        return f"Queue is empty"

    def size(self):
        """
        Returns the number of items in the queue.
        The runtime is constant for returning size of the queue
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value expressing whether or not the list 
        representing the Queue is empty

        Runs in the constant time.
        """
        if self.items:
            return f"queue not empty, has {len(self.items)} items"
        return f"Queue is empty"
