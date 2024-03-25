from collections import deque

class Queue:
    '''
    Queue supporting queueing and
    dequeueing in worst-case O(1) time.
    '''


    def __init__(self, max_size = 30):
        '''
        Initialize this queue to the empty queue.
        
        Parameters
        ----------
        max_size : int
            Maximum number of items contained in this queue. Defaults to 10.
        '''

        self._queue = deque(maxlen=max_size)


    def enqueue(self, item):
        '''
        Queues the passed item (i.e., pushes this item onto the tail of this
        queue).

        If this queue is already full, the item at the head of this queue
        is silently removed from this queue *before* the passed item is
        queued.
        '''

        self._queue.append(item)


    def dequeue(self):
        '''
        Dequeues (i.e., removes) the item at the head of this queue *and*
        returns this item.

        Raises
        ----------
        IndexError
            If this queue is empty.
        '''

        return self._queue.pop()
    
# Test case for the problem
    
# Create a Queue instance with a maximum size of 5
roster = Queue(max_size=30)

# Add students to the roster
roster.enqueue("Alice")
roster.enqueue("Bob")
roster.enqueue("Charlie")
roster.enqueue("David")

# Print out the roster
print("Roster:")
while True:
    try:
        student = roster.dequeue()
        print(student)
    except IndexError:
        break