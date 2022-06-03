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
    
ip1 = [100, 200, 300, 400]
# maxSum(ip1,2)
ip2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# maxSum(ip2,4)

# Sliding window technique for max sum in single loop
def maxSumSlidingWindow(arr, k):
    if len(arr) < k:
        return -1
    existing_sum = sum(arr[:k])
    max_sum = existing_sum
    for i in range(len(arr)-k):
        existing_sum = existing_sum-arr[i]+arr[i+k]
        if max_sum<existing_sum:
            max_sum = existing_sum
    print(max_sum)

# maxSumSlidingWindow(ip2,4)
