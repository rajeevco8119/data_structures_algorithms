def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


string = "ABCDEF"
n = len(string)
a = list(string)


# permute(a, 0, n)


# Next greater element using sliding window
def nextGE(arr):
    aux_arr = []
    flag = 0
    for i in range(len(arr)):
        next = -1
        for k in range(i + 1, len(arr)):
            if arr[i] < arr[k]:
                next = arr[k]
                break
        print(str(next))
    return


arr5 = [11, 13, 21, 3]


# nextGE(arr5)

# print-subarrays-given-array with loops (worst case)

def subarrays(arr):
    for i in range(len(arr)):
        for k in range(i + 1, len(arr)):
            for l in range(i, k):
                print(arr[l])
            print("")


s6 = [1, 2, 3, 4]
# subarrays(s6)

# https://www.geeksforgeeks.org/check-reversing-sub-array-make-array-sorted/ Nice one

## Python3 program to find if there is path from top left to right bottom

row = 5
col = 5


def isPath(arr):
    Dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = [(0, 0)]

    # print(q[0][1])
    while len(q)>0:
        p = q[0]
        q.pop(0)

        arr[p[0]][p[1]] = -1

        if (p == (row-1 , col-1)):
            return True

        for i in range(4):
            a = p[0]+ Dir[i][0]
            b = p[1]+ Dir[i][1]

            if (a >= 0 and b >= 0 and a < row and b < col and arr[a][b] != -1):
                q.append((a,b))
    return False

arr6 = [[ 0, 0, 0, -1, 0 ],
          [ -1, 0, 0, -1, -1],
          [ 0, 0, 0, -1, 0 ],
          [ -1, 0, 0, 0, 0 ],
          [ 0, 0, -1, 0, 0 ] ]
# print(isPath(arr6))

# rn length encoding
# wwwwaaadexxxxxx  w4a3d1e1x6

def printRLE(arr):
    i = 0

    while i < len(arr)-1:
        count = 1
        while i < len(arr)-1 and arr[i] == arr[i+1]:
            count +=1
            i += 1
        i +=1
        print(arr[i-1]+str(count),end="")

st = "wwwwaaadexxxxxxywww"
# printRLE(st)
