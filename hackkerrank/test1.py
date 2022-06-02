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
