class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()

def reverse_string(string):
    reverse_stack = Stack()
    for char in string:
        reverse_stack.push(char)

    reverse_string = ""
    for num in range(reverse_stack.size()):
        reverse_string += reverse_stack.pop()

    return reverse_string

def sort_stack(input_stack: Stack):
    sorted_stack = Stack()
    while input_stack.is_empty() != True:
        temp = input_stack.pop()
        while sorted_stack.is_empty() != True and sorted_stack.peek() > temp:
            input_stack.push( sorted_stack.pop() )
        sorted_stack.push(temp)

    while sorted_stack.is_empty() != True:
        input_stack.push( sorted_stack.pop() )

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        # transfer elements from stack 1 to stack 2
        for _ in range(len(self.stack1)):
            self.stack2.append( self.stack1.pop() )

        # add new element to stack 1
        self.stack1.append(value)

        for _ in range(len(self.stack2)):
            self.stack1.append( self.stack2.pop() )

    def dequeue(self):
        if self.is_empty() == True:
            return None
        else:
            return self.stack1.pop()



    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0



# tests
#####################################################
def test_dequeue():
    # Create a new queue
    q = MyQueue()

    # Enqueue some values
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Output the front of the queue
    print("Front of the queue:", q.peek())

    # Dequeue some values
    print("Dequeued value:", q.dequeue())
    print("Dequeued value:", q.dequeue())

    # Enqueue another value
    q.enqueue(4)

    # Output the front of the queue again
    print("Front of the queue:", q.peek())

    # Dequeue all remaining values
    print("Dequeued value:", q.dequeue())
    print("Dequeued value:", q.dequeue())

    # Check if the queue is empty
    print("Is the queue empty?", q.is_empty())

    # Dequeue from an empty queue and check if it returns None
    print("Dequeued value from empty queue:", q.dequeue())



    """
        EXPECTED OUTPUT:
        ----------------
        Front of the queue: 1
        Dequeued value: 1
        Dequeued value: 2
        Front of the queue: 3
        Dequeued value: 3
        Dequeued value: 4
        Is the queue empty? True
        Dequeued value from empty queue: None

    """

def test_enqueue():
    # Create a new queue
    q = MyQueue()

    # Enqueue some values
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Output the front of the queue
    print("Front of the queue:", q.peek())

    # Check if the queue is empty
    print("Is the queue empty?", q.is_empty())
    print(q.stack1)

def test_sort_stack():
    my_stack = Stack()
    my_stack.push(3)
    my_stack.push(1)
    my_stack.push(5)
    my_stack.push(4)
    my_stack.push(2)

    print("Stack before sort_stack():")
    my_stack.print_stack()

    sort_stack(my_stack)

    print("\nStack after sort_stack:")
    my_stack.print_stack()

    return

def test_reverse_string():
    print( reverse_string("hello") )

def test_is_balanced_parentheses():

    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')
#####################################################

if __name__ == "__main__":
    #test_is_balanced_parentheses()
    #test_reverse_string()
    #test_sort_stack()
    #test_enqueue()
    test_dequeue()