# Time complexity worst

def rotateLeft(d, arr):
    # Write your code here
    while d > 0:
        temp = arr[0]    
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = temp
        d -= 1
    return arr
