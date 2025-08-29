class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        temp = self.root
        while temp is not None:

            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value and temp.left is None:
                temp.left = new_node
                return True
            else:
                temp = temp.left

            if new_node.value > temp.value  and temp.right is None:
                temp.right = new_node
                return True
            else:
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

def test_contains():
    def check(expect, actual, message):
        print(message)
        print("EXPECTED:", expect)
        print("RETURNED:", actual)
        print("PASS" if expect == actual else "FAIL", "\n")

    print("\n----- Test: Contains on Empty Tree -----\n")
    bst = BinarySearchTree()
    result = bst.contains(5)
    check(False, result, "Check if 5 exists in an empty tree:")

    print("\n----- Test: Contains Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    result = bst.contains(10)
    check(True, result, "Check if 10 exists:")
    result = bst.contains(5)
    check(True, result, "Check if 5 exists:")
    result = bst.contains(15)
    check(True, result, "Check if 15 exists:")

    print("\n----- Test: Contains Not Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    result = bst.contains(15)
    check(False, result, "Check if 15 exists:")

    print("\n----- Test: Contains with Duplicate Inserts -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    result = bst.contains(10)
    check(True, result, "Check if 10 exists with duplicate inserts:")



if __name__ == "__main__":
    test_contains()