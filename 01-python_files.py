# Queue Example

print('Good Morning! What food did you put in your pantry')
print("Hit enter after each food added, press 'r' to remove and 'q' to quit")
pantry = []
while True:
    data = input()
    if str.lower(data) =="q":
        break
    elif str.lower(data) =="r":
        print("Removing:", pantry.pop(0))
    else:
        pantry.append(data)
    print(pantry)
print("You have the following food in your pantry:")
for food in pantry:
    print(food)



from collections import deque

class Queue:
    '''
    Thread-safe, memory-efficient, maximally-sized queue supporting queueing and
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