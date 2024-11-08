# lists

# 1
arr1 = [0,1,2,3,4,5,6,7,8,9]
arr2 = [8,6,4,2]

# 2
print(arr1[0])

# 3
arr2[-1] = -2
print(arr2)

# 4

arr_combined = arr1 + arr2
print(arr_combined)

# 5
arr_sliced = arr_combined[::3]
print(arr_sliced)

# 6
arr_combined.append(1)
arr_combined.append(2)
print(arr_combined)

# 7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_elements_from_combined_lists = list(set(a) & set(b))
print(unique_elements_from_combined_lists)

# 8
c = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
unique_elements = set(c)
print(unique_elements)