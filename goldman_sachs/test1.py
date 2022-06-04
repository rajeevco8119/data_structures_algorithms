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
    index = no*(no+1)//2
    for i in range(0,index):
        s += i
        aux_arr.append(s)
    for k in aux_arr:
        if k-no == 0 or k-no in aux_arr:
            count += 1
    return count-1

# print(consectiveNosum(10))
