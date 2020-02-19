# 1. Given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, 
# write a function rotate_image that receives a matrix as input and rotates the image by 90 degrees in the counter-clockwise direction.
"""
Javascript solution
function rotateImage(arr) {
 arr.forEach(row => row.reverse());
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      [arr[i][j], arr[j][i]] = [arr[j][i], arr[i][j]];
    }
  }

  return arr;
}
"""

def rotateImage(A): 
    N = len(A[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp 
  
# Function to print the matrix 
def printMatrix(A): 
    N = len(A[0]) 
    for i in range(N): 
        print(A[i]) 
  
# Driver code 
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8],  
     [9, 10, 11, 12],  
     [13, 14, 15, 16]] 
rotate90Clockwise(A) 
printMatrix(A) 

# 2. Classify the runtimes of each of the following functions:

def foo(n):
  sq_root = int(math.sqrt(n))
  for i in range(0, sq_root):
    print(i)


def bar(x):
  sum = 0
  for i in range(0, 1463):
    i += sum
    for j in range(0, x):
      for k in range(x, x + 15):
        sum += 1


def baz(array):
  print(array[1])
  midpoint = len(array) // 2
  for i in range(0, midpoint):
    print(array[i])
  for _ in range(1000):
    print('hi')