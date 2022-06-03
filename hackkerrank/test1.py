# Time complexity worst

def rotateLeft(d, arr):
    while d > 0:
        temp = arr[0]    
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = temp
        d -= 1
    return arr

# Rotate in single loop
def rotateLeft(d, arr):
    temp = []
    for i in range(0,d):
        temp.append(arr[i])
    arr = arr[d:]
    return arr+temp

def matchingStrings(strings, queries):
    # Write your code here
    counts = []
    for i in queries:
        count = 0
        for j in strings:
            if j == i:
                count += 1
        counts.append(count)
    return counts

# Largest sum contiguous subarray using Kadane's algorithm
def maxSumSubarraySum(arr):
    max_so_far,max_ending_here = 0,0
    for i in range(len(arr)):
        max_so_far += arr[i]

        if max_ending_here<max_so_far:
            max_ending_here = max_so_far
        if max_so_far < 0:
            max_so_far = 0
    return max_ending_here

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(maxSumSubarraySum(a))
