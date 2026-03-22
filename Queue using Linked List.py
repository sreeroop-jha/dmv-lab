
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)

        if not self.rear:
            self.front = self.rear = new
            return

        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front:
            print("Queue is Empty")
            return None

        removed = self.front.data
        self.front = self.front.next

        if not self.front:  # queue became empty
            self.rear = None

        return removed

    def display(self):
        if not self.front:
            print("Queue is Empty")
            return

        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

q = QueueLL()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.dequeue())

q.display()
