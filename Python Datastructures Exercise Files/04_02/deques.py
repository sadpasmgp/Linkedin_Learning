#Deque - Double ended queue

class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
        Takes an item as a parametr and inserts it into
        0th index of the list that is representing Deque

        The runtme is linear or 0(n) or constant time
        """
        self.items.insert(0, item)
        

    def add_rear(self, item):
        """
        Takes an item as a parametr and inserts it into
        last index of the list that is representing Deque

        The runtme is linear or 0(n) or constant time
        """
        self.items.append(item)
        

    def remove_front(self):
        """
        Takes an item as a parametr and removes it from
        0th index of the list that is representing Deque

        The runtme is linear or 0(n) or constant time
        """
        if self.items:
            return self.items.pop(0)
        return "Deque empty"

    def remove_rear(self):
        """
        Takes an item as a parametr and removes it from
        last index of the list that is representing Deque

        The runtme is linear or 0(n) or constant time
        """
        if self.items:
            return self.items.pop()
        return "Deque empty"

    def peek_front(self):
        """
        Takes an item as a parametr and displays
        0th index of the list that is representing Deque

        The runtme is linear or 0(n) or constant time
        """
        if self.items:
            return self.items[0]
        return "Deque empty"

    def peek_rear(self):
        """
        Takes an item as a parametr and displays from
        last index of the list that is representing Deque

        The runtme is linear or 0(n) or constant time
        """
        if self.items:
            return self.items[-1]
        return "Deque empty"

    def size(self):
        """
        Displays size of the Deque

        The runtme is linear or 0(n) or constant time
        """


        return f"size : {len(self.items)}"

    def is_empty(self):
        """
        If size of the Deque is zero, then returns deque is empty

        The runtme is linear or 0(n) or constant time
        """
        if len(self.items) == 0:
            return "Deque empty"
        return f"Deque has {len(self.items)} elements"
