class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] < self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] < self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

def find_kth_smallest(nums, k):
    heap = MaxHeap()
    for num in nums:
        heap.insert(num)

    heap_len = len(heap.heap)
    print(heap_len-k)
    for i in range(heap_len):
        removed = heap.remove()
        if i == (heap_len-k):
            return removed

def stream_max(nums: list):
    heap = MaxHeap()
    max_stream = []
    for num in nums:
        heap.insert(num)
        #print(f"max num: {heap.heap[0]}")
        max_stream.append(heap.heap[0])
    return max_stream


def test_stream_max():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
        ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = stream_max(nums)
        print(f'\nTest {i+1}')
        print(f'Input: {nums}')
        print(f'Expected Output: {expected}')
        print(f'Actual Output: {result}')
        if result == expected:
            print('Status: Passed')
        else:
            print('Status: Failed')


def test_find_kth_smallest():
    # Test cases
    nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
    ks = [2, 3, 4, 7]
    expected_outputs = [2, 3, 4, 5]

    for i in range(len(nums)):
        print(f'Test case {i+1}...')
        print(f'Input: {nums[i]} with k = {ks[i]}')
        result = find_kth_smallest(nums[i], ks[i])
        print(f'Output: {result}')
        print(f'Expected output: {expected_outputs[i]}')
        print(f'Test passed: {result == expected_outputs[i]}')
        print('---------------------------------------')

def test_max_heap():
        # Max heap
    #--------------------------------------------------------------
    myheap = MaxHeap()
    myheap.insert(95)
    myheap.insert(75)
    myheap.insert(80)
    myheap.insert(55)
    myheap.insert(60)
    myheap.insert(50)
    myheap.insert(65)

    print(myheap.heap)


    myheap.remove()

    print(myheap.heap)


    myheap.remove()

    print(myheap.heap)


    """
        EXPECTED OUTPUT:
        ----------------
        [95, 75, 80, 55, 60, 50, 65]
        [80, 75, 65, 55, 60, 50]
        [75, 60, 65, 55, 50]

    """

def test_min_heap():
    # min heap
    #--------------------------------------------------------------
    myheap = MinHeap()
    myheap.insert(12)
    myheap.insert(10)
    myheap.insert(8)
    myheap.insert(6)
    myheap.insert(4)
    myheap.insert(2)

    print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

    removed = myheap.remove()
    print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

    removed = myheap.remove()
    print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

    removed = myheap.remove()
    print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]



    """
        EXPECTED OUTPUT:
        ----------------
        [2, 6, 4, 12, 8, 10]
        Removed: 2, Heap: [4, 6, 10, 12, 8]
        Removed: 4, Heap: [6, 8, 10, 12]
        Removed: 6, Heap: [8, 12, 10]

    """
    #--------------------------------------------------------------

if __name__ == "__main__":
    #test_max_heap()
    #test_min_heap()
    #test_find_kth_smallest()
    test_stream_max()