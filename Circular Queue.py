class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return None

        removed = self.q[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return removed

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        i = self.front
        while True:
            print(self.q[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

print("Dequeued:", cq.dequeue())

cq.display()
