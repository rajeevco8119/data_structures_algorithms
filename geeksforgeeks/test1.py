# Assuption is that arr is strictly increasing with only exception at pivot
def pivotSort(arr, key):
    pivot = 0
    for i in range(len(arr)):
        if arr[i] < arr[i - 1]:
            pivot = i
    print(pivot)
    temp1 = arr[pivot:]
    temp2 = arr[:pivot]
    arr = temp1 + temp2
    return arr


a3 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# print(pivotSort(a3))

def subArraySum(arr, s):
    sum, i, k = 0, 0, 0
    while k != len(arr):
        if sum == s:
            return i + 1, k
        elif sum < s:
            k += 1
            sum += arr[k]
        else:
            i += 1
            sum -= arr[i]
    return False


a4 = [1, 2, 3, 7, 5]
# print(subArraySum(a4,10))


# Reverse an array in groups of given size
def reverseArrGroup(arr, k):
    i = 0
    n = len(arr)
    while i < n:
        left = i
        right = min(n-1,i+k-1)

        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        i += k
    print(arr)
    return


a5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# reverseArrGroup(a5,3)
