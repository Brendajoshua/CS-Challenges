#Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.

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
