def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append( list1[i] )
            i+=1
        else:
            combined.append( list2[j] )
            j+=1

    if i == len(list1) and j < len(list2):
        combined += list2[j:]

    if i < len(list1) and j == len(list2):
        combined += list1[i:]


    return combined 


if __name__ == "__main__":
    print(merge([1,2,7,8], [3,4,5,6]))