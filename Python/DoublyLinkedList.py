class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head.next
        print(f"\nprev: {self.head.prev} \t curr: {self.head.value}")
        while temp is not None:
            #print(temp.value)
            print(f"prev: {temp.prev.value} \t curr: {temp.value}")
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        remove_node = None
        if index < 0 or index >= self.length:
            remove_node = None
        elif index == 0:
            remove_node = self.pop_first()
        elif index == self.length - 1:
            remove_node = self.pop()
        elif index > 0 or index < self.length - 1:
            remove_node = self.get(index)
            before = remove_node.prev
            after = remove_node.next

            remove_node.prev = None
            remove_node.next = None

            before.next = after
            after.prev = before
            self.length -= 1

        return remove_node

    def is_palindrome(self):
        palindrome_state = True
        if self.length == 2:
            up = self.head
            down = up.next
            if up.value == down.value:
                palindrome_state = True
            else:
                palindrome_state = False
        else:
            current_node = self.head
            index = 0

            mid_node = None
            mid_index = int(self.length/2)

            # find mid index point
            while current_node:
                if index == mid_index:
                    mid_node = current_node
                current_node = current_node.next
                index += 1

            # check palindrome condition
            up = mid_node
            down = mid_node

            while up and down:
                if up.value != down.value:
                    palindrome_state = False
                up = up.next
                down = down.prev
        return palindrome_state

    def reverse(self):
        curr = self.head

        while curr:
            after = curr.next
            curr.next = curr.prev
            curr.prev = after
            curr = after

        temp = self.head
        self.head = self.tail
        self.tail = temp

    def partition_list(self, x):
        def print_list(head: Node):
            temp = head
            while temp is not None:
                print(temp.value)
                temp = temp.next

        dummy1 = Node(0)
        list1 = dummy1
        dummy2 = Node(0)
        list2 = dummy2

        temp = self.head
        prev = None
        while temp:
            curr = self.head
            if temp.value < x:
                list1.next = curr
                list1 = curr

                prev = curr
                self.head = temp.next
                temp = temp.next

            elif temp.value >= x:
                list2.next = curr
                list2 = curr

                curr.prev = prev
                prev = curr
                self.head = temp.next
                temp = temp.next


        list1.next = None
        list2.next = None

        list1.next = dummy2.next
        self.head = dummy1.next

        # set previous pointers
        temp = self.head
        prev = None
        while temp:
            temp.prev = prev
            prev = temp
            temp = temp.next

    def reverse_between(self, start_idx, end_idx):
        def print_list(head: Node):
            temp = head
            while temp is not None:
                print(temp.value)
                temp = temp.next

        def reverse_sublist(head: Node, tail: Node) -> tuple:
            curr = head

            while curr:

                after = curr.next
                curr.next = curr.prev
                curr.prev = after
                curr = after
            temp = head
            head = tail
            tail = temp
            return (tail, head)

        if end_idx - start_idx == 0:
            return
        elif self.length == 0:
            return
        elif start_idx == 0 and end_idx == self.length-1:
            (self.tail, self.head) = reverse_sublist(self.head, self.tail)
        else:
            # extract sublist
            temp = self.head
            idx = 0
            sublist_head = None
            sublist_head_prev = None
            sublist_tail = None
            sublist_tail_after = None
            while temp:
                if idx == start_idx:
                    sublist_head = temp
                    sublist_head_prev = temp.prev
                    temp.prev = None

                if idx == end_idx:
                    sublist_tail = temp
                    sublist_tail_after = temp.next
                    temp.next = None

                idx += 1
                temp = temp.next

            (sublist_tail, sublist_head) = reverse_sublist(sublist_head, sublist_tail)

            #reconnect to the rest of the list
            sublist_head_prev.next = sublist_head
            sublist_head.prev = sublist_head_prev

            sublist_tail.next = sublist_tail_after
            sublist_tail_after.prev = sublist_tail

        return

    def swap_pairs(self):
        if self.length == 0:
            return

        def print_list(head: Node):
            temp = head
            while temp is not None:
                print(temp.value)
                temp = temp.next

        dummy = Node(0)
        dummy.next = self.head
        temp = dummy
        index = 0

        while temp is not None:
            position = index+1
            if position % 2 != 0 and position < self.length:

                first = temp.next
                second = first.next

                first.next = second.next
                first.prev = second

                second.next = first
                second.prev = temp
                temp.next = second

            index += 1
            temp = temp.next

        self.head = dummy.next
        self.head.prev = None
        return

def swap_pairs_test():
    my_dll = DoublyLinkedList(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.append(4)

    print('my_dll before swap_pairs:')
    my_dll.print_list()

    my_dll.swap_pairs()


    print('my_dll after swap_pairs:')
    my_dll.print_list()


    """
        EXPECTED OUTPUT:
        ----------------
        my_dll before swap_pairs:
        1 <-> 2 <-> 3 <-> 4
        ------------------------
        my_dll after swap_pairs:
        2 <-> 1 <-> 4 <-> 3

"""

def reverse_between_test():

    # Test Cases
    print("\nTest 1: Middle segment reversal")
    dll1 = DoublyLinkedList(3)
    for v in [8, 5, 10, 2, 1]:
        dll1.append(v)
    print("BEFORE: ", end="")
    dll1.print_list()
    dll1.reverse_between(1, 4)
    print("AFTER:  ", end="")
    dll1.print_list()


    print("\nTest 2: Full list reversal")
    dll2 = DoublyLinkedList(1)
    for v in [2, 3, 4, 5]:
        dll2.append(v)
    print("BEFORE: ", end="")
    dll2.print_list()
    dll2.reverse_between(0, 4)
    print("AFTER:  ", end="")
    dll2.print_list()

    print("\nTest 3: No-op on single node")
    dll3 = DoublyLinkedList(9)
    print("BEFORE: ", end="")
    dll3.print_list()
    dll3.reverse_between(0, 0)
    print("AFTER:  ", end="")
    dll3.print_list()

    print("\nTest 4: Reversal with head involved")
    dll4 = DoublyLinkedList(7)
    for v in [8, 9]:
        dll4.append(v)
    print("BEFORE: ", end="")
    dll4.print_list()
    dll4.reverse_between(0, 2)
    print("AFTER:  ", end="")
    dll4.print_list()

def partition_list_test():
    # -------------------------------
    # Test Cases:
    # -------------------------------

    print("\nTest Case 1: Partition around 5")
    dll1 = DoublyLinkedList(3)
    dll1.append(8)
    dll1.append(5)
    dll1.append(10)
    dll1.append(2)
    dll1.append(1)
    print("BEFORE: \n", end="")
    dll1.print_list()
    dll1.partition_list(5)
    print("AFTER: \n", end="")
    dll1.print_list()

    print("\nTest Case 2: All nodes less than x")
    dll2 = DoublyLinkedList(1)
    dll2.append(2)
    dll2.append(3)
    print("BEFORE: ", end="")
    dll2.print_list()
    dll2.partition_list(5)
    print("AFTER:  ", end="")
    dll2.print_list()

    print("\nTest Case 3: All nodes greater than x")
    dll3 = DoublyLinkedList(6)
    dll3.append(7)
    dll3.append(8)
    print("BEFORE: ", end="")
    dll3.print_list()
    dll3.partition_list(5)
    print("AFTER:  ", end="")
    dll3.print_list()

    print("\nTest Case 4: Empty list")
    dll4 = DoublyLinkedList(1)
    dll4.make_empty()
    print("BEFORE: ", end="")
    dll4.print_list()
    dll4.partition_list(5)
    print("AFTER:  ", end="")
    dll4.print_list()

    print("\nTest Case 5: Single node")
    dll5 = DoublyLinkedList(1)
    print("BEFORE: ", end="")
    dll5.print_list()
    dll5.partition_list(5)
    print("AFTER:  ", end="")
    dll5.print_list()

def is_palindrome_test():
    my_dll_1 = DoublyLinkedList(1)
    my_dll_1.append(2)
    my_dll_1.append(3)
    my_dll_1.append(2)
    my_dll_1.append(1)

    print('my_dll_1 is_palindrome:')
    print( my_dll_1.is_palindrome() )

    my_dll_2 = DoublyLinkedList(1)
    my_dll_2.append(2)
    my_dll_2.append(3)

    print('\nmy_dll_2 is_palindrome:')
    print( my_dll_2.is_palindrome() )



    """
        EXPECTED OUTPUT:
        ----------------
        my_dll_1 is_palindrome:
        True

        my_dll_2 is_palindrome:
        False

    """

def reverse_test():
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(5)


    print('DLL before reverse():')
    my_doubly_linked_list.print_list()


    my_doubly_linked_list.reverse()


    print('\nDLL after reverse():')
    my_doubly_linked_list.print_list()



    """
        EXPECTED OUTPUT:
        ----------------
        DLL before reverse():
        1 <-> 2 <-> 3 <-> 4 <-> 5

        DLL after reverse():
        5 <-> 4 <-> 3 <-> 2 <-> 1

    """

if __name__ == "__main__":
    #is_palindrome_test()
    #reverse_test()
    #partition_list_test()
    #reverse_between_test()
    swap_pairs_test()