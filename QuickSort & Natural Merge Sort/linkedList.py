class Node:

    def __init__(self, data=None, next=None):

        self.data = data
        self.next = next
        
class Segment:
    def __init__(self, size, head, tail):
        self.size = size
        self.head = head
        self.tail = tail

class linkedList:

    def __init__(self, head=None):

        self.head = head

    def length(self):

        i = 0

        if self.head == None:
            return i
        else:
            temp = self.head
            while temp != None:

                i += 1

                temp = temp.next

        return i

    def toArray(self):

        re = []
        if self.head == None:
            return []
        else:
            temp = self.head
            while temp != None:

                re.append(temp.data)
                temp = temp.next
        return re

    def get(self, index):

        i = 0
        temp = self.head

        if index < 0:
            return None
        else:
            while i != index:
                temp = temp.next
                i += 1
        return temp
                









        
        
            
        
