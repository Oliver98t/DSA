def remove_element(nums: list, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

def find_max_min(nums: list):
    max = nums[0]
    min = nums[0]
    for num in nums[1:]:
        if max < num:
            max = num

        if min > num:
            min = num

    return (max, min)

def find_longest_string(strings: list[str]):
    max_string = strings[0]

    for string in strings[1:]:
        if len(string) > len(max_string):
            max_string = string

    return max_string

def remove_duplicates(nums):
    if not nums:
        return 0

    write_pointer = 1

    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1

    return write_pointer

def max_profit(nums: list):
    max_profit = 0

    for buy_idx in range(len(nums)):

        for sell_idx in range(buy_idx+1, len(nums)):

            profit = nums[sell_idx] - nums[buy_idx]
            if max_profit < profit:
                max_profit = profit

    return max_profit

def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

def max_subarray(nums: list):
    if not nums:
        return 0
    max_sum = nums[0]
    for start_num_idx in range(len(nums)):
        sum = 0
        for end_num_idx in range(start_num_idx, len(nums)):
            sum += nums[end_num_idx]
            if sum > max_sum:
                max_sum = sum

    return max_sum


# test functions
def test_max_subarray():
    # Example 1: Simple case with positive and negative numbers
    input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result_1 = max_subarray(input_case_1)
    print("Example 1: Input:", input_case_1, "\nResult:", result_1)


    # Example 2: Case with a negative number in the middle
    input_case_2 = [1, 2, 3, -4, 5, 6]
    result_2 = max_subarray(input_case_2)
    print("Example 2: Input:", input_case_2, "\nResult:", result_2)

    # Example 3: Case with all negative numbers
    input_case_3 = [-1, -2, -3, -4, -5]
    result_3 = max_subarray(input_case_3)
    print("Example 3: Input:", input_case_3, "\nResult:", result_3)


def test_rotate():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print("Rotated array:", nums)

def test_max_profit():
    prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(prices)
    print("Test with mixed prices:")
    print("Prices:", prices)
    print("Maximum profit:", profit)
    print("-----------------------------")


    prices = [7, 6, 4, 3, 1]
    profit = max_profit(prices)
    print("Test with descending prices:")
    print("Prices:", prices)
    print("Maximum profit:", profit)
    print("-----------------------------")


    prices = [1, 2, 3, 4, 5, 6]
    profit = max_profit(prices)
    print("Test with ascending prices:")
    print("Prices:", prices)
    print("Maximum profit:", profit)
    print("-----------------------------")

def test_remove_duplicates():

    # Test case 1: Empty list
    test1 = []
    print(f"Test 1 Before: {test1}")
    result1 = remove_duplicates(test1)
    print(f"Test 1 After: {test1[:result1]}")
    print(f"New Length: {result1}")
    print("------")

    # Test case 2: List with all duplicates
    test2 = [1, 1, 1, 1, 1]
    print(f"Test 2 Before: {test2}")
    result2 = remove_duplicates(test2)
    print(f"Test 2 After: {test2[:result2]}")
    print(f"New Length: {result2}")
    print("------")

    # Test case 3: List with no duplicates
    test3 = [1, 2, 3, 4, 5]
    print(f"Test 3 Before: {test3}")
    result3 = remove_duplicates(test3)
    print(f"Test 3 After: {test3[:result3]}")
    print(f"New Length: {result3}")
    print("------")


    # Test case 4: List with some duplicates
    test4 = [1, 1, 2, 2, 3, 4, 5, 5]
    print(f"Test 4 Before: {test4}")
    result4 = remove_duplicates(test4)
    print(f"Test 4 After: {test4[:result4]}")
    print(f"New Length: {result4}")
    print("------")

def test_find_longest_string():
    string_list = ['apple', 'banana', 'kiwi', 'pear']
    longest = find_longest_string(string_list)
    print(longest)

def test_find_max_min():
    print( find_max_min([5, 3, 8, 1, 6, 9]) )

def test_remove_element():

    # Test case 1: Removing a single instance of a value (1) in the middle of the list.
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    val1 = 1
    print("\nRemove a single instance of value", val1, "in the middle of the list.")
    print("BEFORE:", nums1)
    new_length1 = remove_element(nums1, val1)
    print("AFTER:", nums1, "\nNew length:", new_length1)
    print("-----------------------------------")


    # Test case 2: Removing a value that's located at the end of the list.
    nums2 = [1, 2, 3, 4, 5, 6]
    val2 = 6
    print("\nRemove value", val2, "that's located at the end of the list.")
    print("BEFORE:", nums2)
    new_length2 = remove_element(nums2, val2)
    print("AFTER:", nums2, "\nNew length:", new_length2)
    print("-----------------------------------")

    # Test case 3: Removing a value that's located at the start of the list.
    nums3 = [-1, -2, -3, -4, -5]
    val3 = -1
    print("\nRemove value", val3, "that's located at the start of the list.")
    print("BEFORE:", nums3)
    new_length3 = remove_element(nums3, val3)
    print("AFTER:", nums3, "\nNew length:", new_length3)
    print("-----------------------------------")

    # Test case 4: Attempting to remove a value from an empty list.
    nums4 = []
    val4 = 1
    print("\nAttempt to remove value", val4, "from an empty list.")
    print("BEFORE:", nums4)
    new_length4 = remove_element(nums4, val4)
    print("AFTER:", nums4, "\nNew length:", new_length4)
    print("-----------------------------------")

    # Test case 5: Removing all instances of a repeated value.
    nums5 = [1, 1, 1, 1, 1]
    val5 = 1
    print("\nRemove all instances of value", val5, "from the list.")
    print("BEFORE:", nums5)
    new_length5 = remove_element(nums5, val5)
    print("AFTER:", nums5, "\nNew length:", new_length5)
    print("-----------------------------------")

if __name__ == "__main__":
    #test_remove_element()
    #test_find_max_min()
    #test_find_longest_string()
    #test_remove_duplicates()
    #test_max_profit()
    #test_rotate()
    test_max_subarray()