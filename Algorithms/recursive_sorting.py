# 1. Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.

def binary_search_recursive(arr, target, low, high):
  
  middle = (low + high) // 2

  if len(arr) == 0:
    return -1 
  if arr[middle] == target:
    return middle
  elif arr[middle] > target:
    high = middle - 1
    return binary_search_recursive(arr, target, low, high)
  else:
    low = middle + 1
return binary_search_recursive(arr, target, low, high)

# 2. What would be the base case(s) we’d have to consider for implementing this function?

#line 7 would be our base case such that when the length of the array is 0, execution stops.

# 3. How should our recursive solution converge on our base case(s)?
