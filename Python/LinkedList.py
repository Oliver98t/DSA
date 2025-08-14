class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
        # Instead of the for loop you could use:
        # while temp is not None:
        # -- or --
        # while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def make_empty(self):
        self.head = None
        self.length = 0

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            print("---------------------")
            print(f"slow: {slow.value}")
            print(f"fast: {fast.value}")
            print("---------------------\n")
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        # means ther is no loop
        return False

    def remove_duplicates(self):
        inspect = self.head
        inspect_index = 0
        current_index = 0
        while inspect is not None:
            current = self.head
            prev = self.head
            #--------------------------------
            while current is not None:
                if inspect.value == current.value and current_index != inspect_index:
                    prev.next = current.next
                current_index += 1
                prev = current
                current = current.next
            #--------------------------------
            current_index = 0
            inspect_index += 1
            inspect = inspect.next

    def binary_to_decimal(self):
        binary_position = self.head
        list_len = 0
        # get length of binary list
        while binary_position is not None:
            list_len += 1
            binary_position = binary_position.next

        binary_position = self.head
        binary_index = 0
        decimal_num = 0
        while binary_position is not None:
            print(binary_position.value)
            if binary_position.value == 1:
                decimal_num += pow(2, list_len-binary_index-1)

            binary_index += 1
            binary_position = binary_position.next

        return decimal_num

    def partition_list(self, x):
        dummy1 = Node(0)
        prev1 = dummy1
        dummy2 = Node(0)
        prev2 = dummy2

        def print_dummy(dummy):
            while dummy is not None:
                print(dummy.value)
                dummy = dummy.next


        temp = self.head
        while temp is not None:
            if x > temp.value:
                prev = self.head
                prev1.next = prev
                prev1 = prev

                self.head = temp.next
                temp = temp.next


            elif x <= temp.value:
                prev = self.head
                prev2.next = prev
                prev2 = prev
                self.head = temp.next
                temp = temp.next

        prev1.next = None
        prev2.next = None

        prev1.next = dummy2.next


        self.head = dummy1.next

    def reverse_between(self, start_index, end_index):
        if end_index - start_index == 0:
            return
        if self.length == 0:
            return

        def print_sub_list(head: Node):
            temp = head
            while temp:
                print(temp.value)
                temp = temp.next

        def reverse_sub_list(head: Node, sub_list_len: int):
            curr = head
            prev = None

            while curr is not None:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after

            return prev
        # extract sublist
        #################################################
        temp = self.head
        previous = None
        index = 0
        # sub list variables
        sub_head = None
        prev_sub_head = None
        sub_tail = None
        after_sub_tail = None

        while temp is not None:

            if index == start_index and index == 0:
                sub_head = temp
                prev_sub_head = temp
            elif index == start_index:
                sub_head = temp
                prev_sub_head = previous

            if index == end_index:
                sub_tail = temp

                if temp.next is None:
                    after_sub_tail = temp

                else:
                    after_sub_tail = temp.next

                sub_tail.next = None

            index += 1
            previous = temp
            temp = temp.next
        #################################################

        # perform reverse on sub list
        #################################################
        sub_tail = sub_head
        sub_head = reverse_sub_list(sub_head, (end_index-start_index)+1)

        if start_index != 0:

            prev_sub_head.next = sub_head
        else:
            self.head = sub_head


        if (self.length-1) == end_index:
            sub_tail.next = None
        else:
            sub_tail.next = after_sub_tail
        #################################################

    def swap_pairs(self):
        dummy1 = Node(0)
        dummy1.next = self.head
        prev = dummy1
        index = 0

        while prev is not None:
            position = index+1
            if position % 2 != 0 and position < self.length:

                first = prev.next
                second = first.next

                first.next = second.next
                second.next = first
                prev.next = second


            index += 1
            prev = prev.next

        self.head = dummy1.next

def find_kth_from_end(ll: LinkedList, k):
    slow = ll.head
    fast = ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

# test cases
def swap_pairs_test():
    # Test case 1: Swapping pairs in a list with an even number of nodes (1->2->3->4)
    print("\nTest case 1: Swapping pairs in a list with an even number of nodes.")
    ll1 = LinkedList(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    print("BEFORE: ", end="")
    ll1.print_list()

    ll1.swap_pairs()
    print("AFTER:  ", end="")
    ll1.print_list()
    print("-----------------------------------")

    #'''
    # Test case 2: Swapping pairs in a list with an odd number of nodes (1->2->3->4->5)
    print("\nTest case 2: Swapping pairs in a list with an odd number of nodes.")
    ll2 = LinkedList(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    ll2.append(5)
    print("BEFORE: ", end="")
    ll2.print_list()
    print("AFTER:  ", end="")
    ll2.swap_pairs()
    ll2.print_list()
    print("-----------------------------------")

    # Test case 3: Swapping pairs in a list with a single node (1)
    print("\nTest case 3: Swapping pairs in a list with a single node.")
    ll3 = LinkedList(1)
    print("BEFORE: ", end="")
    ll3.print_list()
    print("AFTER:  ", end="")
    ll3.swap_pairs()
    ll3.print_list()
    print("-----------------------------------")

    # Test case 4: Swapping pairs in an empty list
    print("\nTest case 4: Swapping pairs in an empty list.")
    ll4 = LinkedList(1)
    ll4.make_empty()
    print("BEFORE: ", end="")
    ll4.print_list()
    print("AFTER:  ", end="")
    ll4.swap_pairs()
    ll4.print_list()
    print("-----------------------------------")

    # Test case 5: Swapping pairs in a list with two nodes (1->2)
    print("\nTest case 5: Swapping pairs in a list with two nodes.")
    ll5 = LinkedList(1)
    ll5.append(2)
    print("BEFORE: ", end="")
    ll5.print_list()
    print("AFTER:  ", end="")
    ll5.swap_pairs()
    ll5.print_list()
    print("-----------------------------------")
    #'''

def reverse_between_test():
    # test cases
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print("Original linked list: ")
    linked_list.print_list()

    # Reverse a sublist within the linked list
    linked_list.reverse_between(1, 3)
    print("Reversed sublist (2, 4): ")
    linked_list.print_list()


    # Reverse another sublist within the linked list
    linked_list.reverse_between(0, 4)
    print("Reversed entire linked list: ")
    linked_list.print_list()

    #'''
    # Reverse a sublist of length 1 within the linked list
    linked_list.reverse_between(3, 3)
    print("Reversed sublist of length 1 (3, 3): ")
    linked_list.print_list()

    # Reverse an empty linked list
    empty_list = LinkedList(0)
    empty_list.make_empty()
    empty_list.reverse_between(0, 0)
    print("Reversed empty linked list: ")
    empty_list.print_list()
    #'''

def partition_list_test():
    def linkedlist_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)

    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")

def binary_to_decimal_test():

    # Test case 1: Binary number 110 = Decimal number 6
    linked_list = LinkedList(1)
    linked_list.append(1)
    linked_list.append(0)
    print("Test case 1 linked list:")
    linked_list.print_list()
    result = linked_list.binary_to_decimal()
    try:
        assert result == 6
        print("Test case 1 passed, returned:", result)
    except AssertionError:
        print("Test case 1 failed, returned:", result)
    print("-" * 40)


    # Test case 2: Binary number 1000 = Decimal number 8
    linked_list = LinkedList(1)
    linked_list.append(0)
    linked_list.append(0)
    linked_list.append(0)
    print("Test case 2 linked list:")
    linked_list.print_list()
    result = linked_list.binary_to_decimal()
    try:
        assert result == 8
        print("Test case 2 passed, returned:", result)
    except AssertionError:
        print("Test case 2 failed, returned:", result)
    print("-" * 40)


    # Test case 3: Binary number 0 = Decimal number 0
    linked_list = LinkedList(0)
    print("Test case 3 linked list:")
    linked_list.print_list()
    result = linked_list.binary_to_decimal()
    try:
        assert result == 0
        print("Test case 3 passed, returned:", result)
    except AssertionError:
        print("Test case 3 failed, returned:", result)
    print("-" * 40)

    # Test case 4: Binary number 1 = Decimal number 1
    linked_list = LinkedList(1)
    print("Test case 4 linked list:")
    linked_list.print_list()
    result = linked_list.binary_to_decimal()
    try:
        assert result == 1
        print("Test case 4 passed, returned:", result)
    except AssertionError:
        print("Test case 4 failed, returned:", result)
    print("-" * 40)

    # Test case 5: Binary number 1101 = Decimal number 13
    linked_list = LinkedList(1)
    linked_list.append(1)
    linked_list.append(0)
    linked_list.append(1)
    print("Test case 5 linked list:")
    linked_list.print_list()
    result = linked_list.binary_to_decimal()
    try:
        assert result == 13
        print("Test case 5 passed, returned:", result)
    except AssertionError:
        print("Test case 5 failed, returned:", result)
    print("-" * 40)



    """
        EXPECTED OUTPUT:
        ----------------
        Test case 1 linked list:
        1 -> 1 -> 0
        Test case 1 passed, returned: 6
        ----------------------------------------
        Test case 2 linked list:
        1 -> 0 -> 0 -> 0
        Test case 2 passed, returned: 8
        ----------------------------------------
        Test case 3 linked list:
        0
        Test case 3 passed, returned: 0
        ----------------------------------------
        Test case 4 linked list:
        1
        Test case 4 passed, returned: 1
        ----------------------------------------
        Test case 5 linked list:
        1 -> 1 -> 0 -> 1
        Test case 5 passed, returned: 13
    """

def remove_duplicates_test():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.remove_duplicates()
    print("\n")
    ll.print_list()

    # Test 2: List with some duplicates
    ll = LinkedList(1)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll.remove_duplicates()
    ll.print_list()

def find_middle_node_test():
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    print( my_linked_list.find_middle_node().value )

def has_loop_test():
    my_linked_list_1 = LinkedList(1)
    my_linked_list_1.append(2)
    my_linked_list_1.append(3)
    my_linked_list_1.append(4)
    my_linked_list_1.tail.next = my_linked_list_1.head
    print(my_linked_list_1.has_loop() ) # Returns True

    my_linked_list_2 = LinkedList(1)
    my_linked_list_2.append(2)
    my_linked_list_2.append(3)
    my_linked_list_2.append(4)
    print(my_linked_list_2.has_loop() ) # Returns False

def find_kth_from_end_test():
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    k = 1
    result = find_kth_from_end(my_linked_list, k)
    print(result.value)  # Output: 4

if __name__ == "__main__":
    #find_middle_node_test()
    #has_loop_test()
    #find_kth_from_end_test()
    #remove_duplicates_test()
    #binary_to_decimal_test()
    partition_list_test()
    #reverse_between_test()
    #swap_pairs_test()