def rotateLeft(d, arr):
    # Write your code here
    temp = []
    for i in range(0, d):
        temp.append(arr[i])
    arr = arr[d:]
    print(arr + temp)


# arr = [1, 3, 5, 7, 9]


# rotateLeft(2,arr)

def matchingStrings(strings, queries):
    counts = []
    for i in queries:
        count = 0
        for j in strings:
            if j == i:
                count += 1
        counts.append(count)
    return counts


strs = ['ab', 'ab', 'abc']
quer = ['ab', 'abc', 'bc']


# print(matchingStrings(strs,quer))

# Maximum sum using k consecutive elements using sliding window
def maxSum(arr, k):
    sum, max_sum = 0, 0
    for i in range(len(arr) - k + 1):
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
    for i in range(len(arr) - k):
        existing_sum = existing_sum - arr[i] + arr[i + k]
        if max_sum < existing_sum:
            max_sum = existing_sum
    print(max_sum)


ip3 = [100, 200, 300, 400]


# maxSumSlidingWindow(ip2,4)

# Anagram Substring Search (Or Search for all permutations)
def substringSearchAnagram(arr, substr):
    count = 0
    s_len = len(substr)
    ord_sub = 0
    ord_sum = 0
    for i in substr:
        ord_sub += ord(i)
    for i in range(len(arr) - s_len + 1):
        ord_sum = 0
        for j in range(s_len):
            ord_sum += ord(arr[i + j])
        if ord_sum == ord_sub:
            count += 1
    print(count)


# No of substrings with given pattern
def substringsearch(arr, substr):
    count = 0
    s_len = len(substr)

    for i in range(len(arr) - s_len):
        if arr[i:i + s_len] == substr:
            count += 1
    print(count)


txt = "BACDGABCDA"
pat = "ABCD"


# substringsearch(txt, pat)
# substringSearchAnagram(txt,pat)
# def subarrayProduct(arr):
#     prod = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             sub = arr[i:j]


# Largest sum contiguous subarray using Kadane's algorithm LIS
def maxSumSubarraySum(arr):
    max_so_far, max_ending_here = 0, 0
    for i in range(len(arr)):
        max_so_far += arr[i]

        if max_ending_here < max_so_far:
            max_ending_here = max_so_far
        if max_so_far < 0:
            max_so_far = 0
    return max_ending_here


# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(maxSumSubarraySum(a))


# Longest Subarray consisting of unique elements from an Array
def uniqueSubarray1(arr):
    longest = 0
    length = 0
    aux_array = []
    for i in range(len(arr)):
        if longest < length:
            longest = length
        if arr[i] not in aux_array:
            aux_array.append(arr[i])
            length += 1
        else:
            length = 1
            aux_array = []
    return longest


# arr = [1, 2, 3, 4, 5, 1, 2, 3]
# print(uniqueSubarray(arr))


# Two Sum
def twoSum(arr, x):
    arr.sort()
    i = 0
    k = len(arr) - 1
    while i < k:
        if x == arr[i] + arr[k]:
            return [arr[i], arr[k]]
        if x > arr[i] + arr[k]:
            i += 1
        else:
            k -= 1
    return "No"


# sa = [0, -1, 2, -3, 1]
# print(twoSum(sa, -2))

# https://gongybable.medium.com/amazon-oa-question-different-types-of-pages-y-tech-442d5ffb9a56
def book(arr):
    cont = 0
    pass


# sa = '01001'

# Goldman Sachs
def firstnonrepeatingchar(arr):
    map = {}
    for i in arr:
        if i in map.keys():
            map[i] += 1
        else:
            map[i] = 1
    for k, v in map.items():
        if v == 1:
            return k


s = 'geeksforgeeks'
# print(firstnonrepeatingchar(s))

from collections import Counter


def firstNonrepeatingchar2(arr):
    f = Counter(arr)
    for k, v in f.items():
        if v == 1:
            return k


# print(firstNonrepeatingchar2(s))

#  find the number of contiguous subarrays such that the
#  product of the elements of the subarray is less than or equal to a given positive integer k

def productSubarrays(arr, k):
    cont = 0
    for i in range(len(arr)):
        for _ in range(i + 1, len(arr)):
            prod = 1
            prodArr = arr[i:_]
            for l in prodArr:
                prod *= l
            if prod <= k:
                cont += 1
    return cont


array = [1, 2, 3, 4]
k = 10
# print(productSubarrays(array,k))

from math import prod


def productSubarrays2(arr, k):
    coint = 0
    a = 0
    n = len(arr)
    for i in range(len(arr)):
        for _ in range(i + 1, len(arr)):
            if prod(arr[i:_]) <= k:
                coint += 1
            else:
                continue
    return coint


# print(productSubarrays2(array,k))

# Given a number N find the number of ways to write N as a sum of two or more positive consecutive integers
def consectiveNosum(no):
    aux_arr = []
    s = 0
    count = 0
    index = no * (no + 1) // 2
    for i in range(0, index):
        s += i
        aux_arr.append(s)
    for k in aux_arr:
        if k - no == 0 or k - no in aux_arr:
            count += 1
    return count - 1


# print(consectiveNosum(10))

# 2D array to 1D array
def twoDtoOneD(arr):
    pass


# geeksforgeeks.org/insertion-sort/
def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        k = i - 1
        while k >= 0 and key < arr[k]:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k + 1] = key
    print(arr)


arr = [12, 11, 13, 5, 6]


# insertionSort(arr)

def GCD1(a, b):
    if a == 0:
        return b
    return GCD1(b % a, a)


def GCD2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return GCD2(a - b, b)
    return GCD2(a, b - a)


def LCM(arr3):
    gcd = arr3[0]
    prod3 = 1
    for i in range(1, len(arr3)):
        gcd = GCD1(gcd, i)
        prod3 *= arr3[i]
    print(int(prod3) // int(gcd))
    return


arr3 = [1, 2, 8, 3]
LCM(arr3)
