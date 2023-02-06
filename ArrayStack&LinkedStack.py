class ArrayStack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.size() == 0:
            print("Stack is empty.")
        else:
            temp = self.data[-1]
            del self.data[-1]
            return temp
        
    def top(self):
        if self.size() == 0:
            print("Stack is empty.")
        else:
            return self.data[-1]

    def size(self):
        return len(self.data)


# ListNode is the node class for the linked list LinkedStack
class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        new_node = ListNode(value)

        if self.size() == 0:
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def pop(self):
        if self.size() == 0:
            print("Stack is empty.")
        else:
            temp = self.head.data
            self.head = self.head.next
            self.length -= 1

            return temp

    def top(self):
        if self.size() == 0:
            print("Stack is empty.")
        else:
            return self.head.data

    def size(self):
        return self.length


if __name__ == "__main__":
    
    test_stack1 = ArrayStack()

    print("Testing test_stack1 = ArrayStack().")
    print(test_stack1.is_empty())
    test_stack1.push("abc")
    test_stack1.push("def")
    print(test_stack1.pop())
    print(test_stack1.size())
    print(test_stack1.top())
    print(test_stack1.pop())
    print(test_stack1.pop())
    print(test_stack1.top())

    test_stack2 = LinkedStack()

    print("\nTesting test_stack2 = LinkedStack().")
    print(test_stack2.is_empty())
    test_stack2.push("abc")
    test_stack2.push("def")
    print(test_stack2.pop())
    print(test_stack2.size())
    print(test_stack2.top())
    print(test_stack2.pop())
    print(test_stack2.pop())
    print(test_stack2.top())
