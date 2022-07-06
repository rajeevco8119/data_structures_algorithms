# Creating staircase would require square blocks.asked in GS

def stairCase(n):
    i,j = 1,0
    while True:
        if j >= n:
            print(i-1)
            break
        i += 1
        j += i

stairCase(15)
