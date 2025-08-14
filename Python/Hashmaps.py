def item_in_common(list1: list, list2: list):
    is_item_in_common = False
    combined = list1 + list2
    table = {}
    for item in combined:
        if item in table:
            table[item] += 1
            is_item_in_common = True
        else:
            table[item] = 1

    return is_item_in_common

def find_duplicates(nums: list) -> list:
    duplicates_list = []
    duplicates_table = {}
    for num in nums:
        if num in duplicates_table:
            duplicates_table[num] += 1
            if duplicates_table[num] == 2:
                duplicates_list.append(num)
        else:
            duplicates_table[num] = 1

    return duplicates_list

def first_non_repeating_char(string: str):
    string_map = {}
    non_repeating_list = []
    for char in string:
        if char in string_map:
            string_map[char] += 1
            if char in non_repeating_list:
                non_repeating_list.remove(char)
        else:
            string_map[char] = 1
            non_repeating_list.append(char)

    if len(non_repeating_list) > 0:
        return non_repeating_list[0]
    else:
        return None

def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())

def two_sum(nums: list, target: int) -> list:
    two_sum_indices = []
    nums_map = {} # {number: index}
    for i, num in enumerate(nums):
        # build hash map
        if num not in nums_map:
            nums_map[num] = i

        # inspect potential matches
        inspect_key = target-num
        inspect_index = nums_map.get(inspect_key)
        if inspect_index != None and inspect_index != i:
            two_sum_indices.append(inspect_index)
            two_sum_indices.append(i)
            break

    return two_sum_indices

def subarray_sum(nums, target):
    pass

# tests
##########################################
def test_subarray_sum():
    nums = [1, 2, 3, 4, 5]
    target = 9
    print ( subarray_sum(nums, target) )

    nums = [-1, 2, 3, -4, 5]
    target = 0
    print ( subarray_sum(nums, target) )

    nums = [2, 3, 4, 5, 6]
    target = 3
    print ( subarray_sum(nums, target) )

    nums = []
    target = 0
    print ( subarray_sum(nums, target) )

def test_two_sum():
    print(two_sum([5, 1, 7, 2, 9, 3], 10))
    print(two_sum([4, 2, 11, 7, 6, 3], 9))
    print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
    print(two_sum([1, 3, 5, 7, 9], 10))
    print ( two_sum([1, 2, 3, 4, 5], 10) )
    print ( two_sum([1, 2, 3, 4, 5], 7) )
    print ( two_sum([1, 2, 3, 4, 5], 3) )
    print ( two_sum([], 0) )

def test_group_anagrams():
    print("1st set:")
    print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )


    print("\n2nd set:")
    print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

    print("\n3rd set:")
    print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

def test_first_non_repeating_char():
    print( first_non_repeating_char('leetcode') )
    print( first_non_repeating_char('hello') )
    print( first_non_repeating_char('aabbcc') )

def test_find_duplicates():
    print ( find_duplicates([1, 2, 3, 4, 5]) )
    print ( find_duplicates([1, 1, 2, 2, 3]) )

    print ( find_duplicates([1, 1, 1, 1, 1]) )
    print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
    print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
    print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
    print ( find_duplicates([]) )

def test_item_in_common():
    list1 = [1,3,5]
    list2 = [2,4,5]


    print(item_in_common(list1, list2))
##########################################
if __name__ == "__main__":
    #test_item_in_common()
    #test_find_duplicates()
    #test_first_non_repeating_char()
    #test_group_anagrams()
    #test_two_sum()
    test_subarray_sum()