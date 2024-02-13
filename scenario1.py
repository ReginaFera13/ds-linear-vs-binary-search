# Linear Search
def linear_search_unsorted(arr, target):
    # Your code here
    steps = 0
    for num in arr:
        steps += 1
        if num == target:
            return (num, steps)

# Binary Search
def binary_search_unsorted(arr, target):
    # Your code here
    steps = 0
    left = 0
    right = len(arr) -1
    while left <= right:
        steps += 1
        middle = (left + right)//2
        if arr[middle] == target:
            return (middle, steps)
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return (-1, steps)

# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")
