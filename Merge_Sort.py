def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left_arr = num[:mid]
    right_arr = num[mid:]
    merge_two_lists(left_arr, right_arr)


def merge_two_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len(a):
        sorted_list.append(a[i])
        i += 1
    while j < len(b):
        sorted_list.append((b[j]))
        j += 1

    print(sorted_list)


# arr_a = [9, 17, 21, 29, 38]
# arr_b = [4, 10,25, 32,49]
numbers = [9, 17, 21, 29, 38, 4, 10, 25, 32, 49]
merge_sort(numbers)
