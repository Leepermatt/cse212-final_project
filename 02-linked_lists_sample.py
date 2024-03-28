## Create a progrma to handle bank customers arriving in line

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            removed_data = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return removed_data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
bank_queue = Queue()

# Enqueue customers
bank_queue.enqueue("John Smith")
bank_queue.enqueue("Alice Leeper")
bank_queue.enqueue("Robert Adams")

# Display queue
print("Queue after enqueue operations:")
bank_queue.display()

# Dequeue a customer
removed_customer = bank_queue.dequeue()
print(f"Dequeued customer: {removed_customer}")

# Display queue after dequeue operation
print("Queue after dequeue operation:")
bank_queue.display()