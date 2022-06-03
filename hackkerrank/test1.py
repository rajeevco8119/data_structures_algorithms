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

# Maximum sum using k consecutive elements using sliding window
def maxSum(arr, k):
    sum, max_sum = 0, 0
    for i in range(len(arr)-k+1):
        sum = 0
        for j in range(i, i + k):
            sum += arr[j]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)
