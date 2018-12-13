class TwoStackQueue(object):

    def __init__(self):
        print("This class provides method that implement a queue with two stack")
        self.instack = []
        self.outstack = []


    def enqueue(self,element):

        self.instack.append(element)

    def dequeue(self):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()
