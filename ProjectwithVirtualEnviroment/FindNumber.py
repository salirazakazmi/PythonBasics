

def findNumber(arr, k):
    # Loop through each item in the array
    for num in arr:
        # Check if the current item is equal to k
        if num == k:
            return "Yes"

    # If the loop completes without finding k, return "No"
    return "No"

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 6
result = findNumber(arr, k)
print(result)
