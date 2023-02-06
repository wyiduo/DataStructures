class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.back = None


class CircularQueue:
    def __init__(self, max_size):
        self.size = 0
        self.MAX_SIZE = max_size
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.MAX_SIZE == 0:
            print("Cannot enqueue into Circular Queue with MAX_SIZE of 0.")
            return
        elif self.MAX_SIZE == 1:
            new_node = ListNode(data)
            
            self.head = new_node
            self.tail = new_node
            self.size = 1
            return
        else:
            new_node = ListNode(data)

            if self.size == 0:
                self.head = new_node
                self.tail = new_node
                self.size += 1
            elif self.size < self.MAX_SIZE: # normal operation
                self.tail.back = new_node
                new_node.next = self.tail
                self.tail = new_node
                self.size += 1
            else: # will break to else if self.size == self.MAX_SIZE
                # will dequeue the earliest node, then enqueue so size does
                # not exceed MAX_SIZE
                self.head = self.head.back
                self.head.next = None
                
                self.tail.back = new_node
                new_node.next = self.tail
                self.tail = new_node
            return

    def dequeue(self):
        if self.size == 0:
            print("Circular Queue is empty.")
            return
        elif self.MAX_SIZE == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            
            return temp
        else:
            temp = self.head.data
            self.head = self.head.back
            self.head.next = None
            self.size -= 1

            return temp


if __name__ == "__main__":

    test_circular_queue1 = CircularQueue(3)

    print("Testing test_circular_queue1 = CircularQueue(3).")
    print(test_circular_queue1.dequeue())
    test_circular_queue1.enqueue("123")
    test_circular_queue1.enqueue("456")
    test_circular_queue1.enqueue("789")
    test_circular_queue1.enqueue("abc")
    print(test_circular_queue1.dequeue())

    test_circular_queue2 = CircularQueue(0)
    print("\nTesting test_circular_queue2 = CircularQueue(0).")
    test_circular_queue2.enqueue("abc")
    print(test_circular_queue2.dequeue())
    
    test_circular_queue3 = CircularQueue(1)
    print("\nTesting test_circular_queue3 = CircularQueue(1).")
    test_circular_queue3.enqueue("abc")
    print(test_circular_queue3.dequeue())
