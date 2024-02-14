# Linear Search
def linear_search_last_occurrence(arr, target):
    # Your code here
    steps = 0
    indices = []
    for i, num in enumerate(arr):
        steps += 1
        if num == target:
            indices.append(i)
    return (indices[-1], steps)
        

# Binary Search
def binary_search_last_occurrence(arr, target):
    # Your code here
    steps = 0
    idx = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
    # while steps <= 11:
        steps += 1
        middle = (left + right)//2
        if target == arr[middle]:
            idx = middle
            left = middle + 1
        elif target < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return (idx, steps)

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")