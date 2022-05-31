# Time conversion 12 hour format to 24 hour format
def timeConversion(s):
    time = s[:-2]
    if s[8] == 'A':
        if s[0] == '1' and s[1] == '2':
            return '00'+time[2:]
        return time
    elif s[8] == 'P':
        if s[0] == '1' and s[1] == '2':
            return time
        hour = int(time[0]+time[1])
        hour += 12
        new_time = str(hour)+time[2:]
        return new_time

#Staircase
def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        a = n-i
        h = i
        while a > 0:
            print(" ",end="")
            a -= 1
        while h > 0:
            print('#',end="")
            h -= 1
        print('\r')

# Staircase efficient
def staircase2(n):
    for i in range(0,n):
        for _ in range(0, n):
            if i + _ >= n-1:
                print('#',end="")
            else:
                print(' ',end="")
        print('\r')
