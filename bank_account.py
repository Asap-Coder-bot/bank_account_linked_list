class Node(object):

    def __init__ (self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_prev (self):
        return self.prev_node

    def set_prev (self, p):
        self.prev_node = p

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d


class DoublyLinkedList:

    def __init__(self):
        self._head = 0
        self._tail = 0

    def get_size (self):
        return self._head

    def add (self, d):
        new_node = Node (d, self._tail)
        if self._tail:
            self._tail.set_prev(new_node)
        self._tail = new_node
        self._head += 1

    def remove (self, d):
        this_node = self._tail

        while this_node:
            if this_node.get_data() == d:
                next = this_node.get_next()
                prev = this_node.get_prev()
                
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self._tail = this_node
                self._head -= 1
                return True		
            else:
                this_node = this_node.get_next()
        return False 

    def find (self, d):
        this_node = self._tail
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
class BankAccount:
    def __init__(self,firstName, fastName, ID, balance=0):
        self.firstName = firstName
        self.lastName = lastName 
        self.ID = ID 
        self.balance = balance

    def setfirstName(self,firstName):
        self.firstName = firstName

    def setlastName(self,lastName):
        self.lastName = lastName

    def setID(self, ID):
        self.ID = ID

    def getfirstName(self,firstName):
        return self.firstName

    def getlastName(self,lastName):
        return self.lastName

    def getID(self, ID):
        return self.ID

    def deposit(self,amount):
        self.balance+= amountΣ
        return self.balance

    def withdraw(self, amount):
        self.balance-= amount
        return self.balance
        


