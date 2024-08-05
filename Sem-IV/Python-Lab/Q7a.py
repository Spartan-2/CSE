# Develop a python program to create two classes called as Stack and Queue. 
# Provide the necessary data members and methods to display the operations that can be performed on stacks and queues. Test for all type of conditions

class stack:
    top = -1
    def __init__(self):
        self.stk = []
    def push(self,item):
        self.stk.append(item)
        self.top += 1
    def pop(self):
        if self.stk:
            self.stk.pop()
            self.top -= 1
            return
        print("Stack underflow")
    def topret(self):
        if self.stk:
            return self.stk[self.top]
        print("Stack is empty ")
    def display(self):
        print(self.stk)

class queue:
    def __init__(self):
        self.q = []
    def insert(self,item):
        self.q.append(item)
    def remove(self):
        if self.q:
            return self.q.pop(0)
        print("Queue is empty")
    def display(self):
        print(self.q)
    
s = stack()
s.push(45)
s.push(9)
s.push(6)
s.display()

s.pop()
s.display()
print(s.topret())

q = queue()
q.insert(34)
q.insert(89)
q.insert(67)

q.display()
print(q.remove())
q.display()
