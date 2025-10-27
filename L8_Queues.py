class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=0
        self.rear=0
        self.size=size
        self.available=size
    def enqueue(self,item):
        if self.available==0:
            print("queue full")
        else:
            self.queue[self.rear]=item
            self.rear=(self.rear+1)%self.size
            self.available-=1
    def dequeue(self):
        if self.available==self.size:
            print("queue empty")
        else:
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size
            self.available+=1
    def first(self):
        print(self.queue[self.front])
    def last(self):
        print(self.queue[self.rear])
    def printqueue(self):
        print(self.queue)

queue1=Queue(5)
queue1.enqueue(8)
queue1.first()
queue1.last()
queue1.enqueue(6)
queue1.dequeue()
queue1.first()
queue1.printqueue()