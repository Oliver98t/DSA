from math import ceil
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        # Base case: empty segment
        if left > right:
            return None
        mid = (left + right) // 2
        root_node = Node(nums[mid])
        root_node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        root_node.right = self.__sorted_list_to_bst(nums, mid + 1, right)
        return root_node

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def __invert_tree(self, node: Node):
        if node:
            node.left, node.right = node.right, node.left
            self.__invert_tree(node.left)
            self.__invert_tree(node.right)
        return node

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def is_valid_bst(self):
        is_valid = True
        dfs_results = self.dfs_in_order()

        prev = 0
        for num in dfs_results:
            if num < prev:
                is_valid = False

            prev = num

        return is_valid

    def kth_smallest(self, k):
        if self.root is None:
            return None

        count = 0
        result = None
        def traverse(current_node):
            nonlocal count, result
            if current_node.left is not None:
                traverse(current_node.left)
            count += 1
            if count == k:
                result = current_node.value
                return
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result


def test_kth_smallest():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst.kth_smallest(1))  # Expected output: 2
    print(bst.kth_smallest(3))  # Expected output: 4
    print(bst.kth_smallest(6))  # Expected output: 7


    """
        EXPECTED OUTPUT:
        ----------------
        2
        4
        7

    """

def test_validate_bst():
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print("BST is valid:")
    print(my_tree.is_valid_bst())



    """
        EXPECTED OUTPUT:
        ----------------
        BST is valid:
        True

    """

def test_invert():
    def tree_to_list(node):
        """Helper function to convert tree to list level-wise for easy comparison"""
        if not node:
            return []
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.value)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        while result and result[-1] is None:  # Clean up trailing None values
            result.pop()
        return result

    def test_invert_binary_search_tree():
        print("\n--- Testing Inversion of Binary Search Tree ---")
        # Define test scenarios
        scenarios = [
            ("Empty Tree", [], []),
            ("Single Node", [1], [1]),
            ("Tree with Left Child", [2, 1], [2, None, 1]),
            ("Tree with Right Child", [1, 2], [1, 2]),
            ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
            ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
        ]

        for description, setup, expected in scenarios:
            bst = BinarySearchTree()
            for num in setup:
                bst.r_insert(num)
            if description == "Invert Twice":
                bst.invert()  # First inversion
            bst.invert()  # Perform inversion (or second inversion for the specific case)
            result = tree_to_list(bst.root)
            print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
            print(f"Expected: {expected}")
            print(f"Actual:   {result}")

    test_invert_binary_search_tree()

def test_sorted_list_to_bst():
    def check_balanced_and_correct_traversal(bst, expected_traversal):
        is_balanced = bst.is_balanced()
        inorder = bst.inorder_traversal()
        print("Is balanced:", is_balanced)
        print("Inorder traversal:", inorder)
        print("Expected traversal:", expected_traversal)
        if is_balanced and inorder == expected_traversal:
            print("PASS: Tree is balanced and inorder traversal is correct.\n")
        else:
            print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")

    # Test: Convert an empty list
    print("\n----- Test: Convert Empty List -----\n")
    bst = BinarySearchTree()
    bst.sorted_list_to_bst([])
    check_balanced_and_correct_traversal(bst, [])

    # Test: Convert a list with one element
    print("\n----- Test: Convert Single Element List -----\n")
    bst = BinarySearchTree()
    bst.sorted_list_to_bst([10])
    check_balanced_and_correct_traversal(bst, [10])

    # Test: Convert a sorted list with odd number of elements
    print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
    bst = BinarySearchTree()
    bst.sorted_list_to_bst([1, 2, 3, 4, 5])
    check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])


    # Test: Convert a sorted list with even number of elements
    print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
    bst = BinarySearchTree()
    bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
    check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

    # Test: Convert a large sorted list
    print("\n----- Test: Convert Large Sorted List -----\n")
    bst = BinarySearchTree()
    large_sorted_list = list(range(1, 16))  # A list from 1 to 15
    bst.sorted_list_to_bst(large_sorted_list)
    check_balanced_and_correct_traversal(bst, large_sorted_list)

if __name__ == "__main__":
    #test_sorted_list_to_bst()
    #test_invert()
    #test_validate_bst()
    test_kth_smallest()