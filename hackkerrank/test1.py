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


# No of substrings with given pattern
txt = "BACDGABCDA"
pat = "ABCD"

def substringsearch(arr, substr):
    count = 0
    s_len = len(substr)

    for i in range(len(arr) - s_len):
        if arr[i:i + s_len] == substr:
            count += 1
    print(count)
# substringsearch(txt, pat)    


# Anagram Substring Search (Or Search for all permutations) (using order)
def substringSearchAnagram(arr, substr):
    count = 0
    s_len = len(substr)
    ord_sub = 0
    ord_sum = 0
    for i in substr:
        ord_sub += ord(i)
    for i in range(len(arr) - s_len+1):
        ord_sum = 0
        for j in range(s_len):
            ord_sum += ord(arr[i+j])
        if ord_sum == ord_sub:
            count += 1
    print(count)
# substringSearchAnagram(txt,pat)
