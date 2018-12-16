class LinkedListCycleCheck(object):

    def __init__(self,value):

        print("This class provide a method for cycle checking in singly linked list")
        self.value = value
        self.next_node = None

    def cycleCheck(self,node):

        marker1 = node
        marker2 = node

        while marker2 != None and marker2.next_node != None:
            marker1 = marker1.next_node
            marker2 = marker2.next_node.next_node

            if marker1 == marker2:
                return True
        return False


a = LinkedListCycleCheck(1)
b = LinkedListCycleCheck(2)
c = LinkedListCycleCheck(3)

a.next_node = b
b.next_node = c
c.next_node = a

print(b.cycleCheck(c))
