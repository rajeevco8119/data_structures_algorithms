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
 

# Hashing Freqency

def hashingFreqency(s):
    # Write your code here
    napp = {}
    res = ''
    for i in range(len(s)):
        if s[i] in napp.keys():
            napp[s[i]] += 1
        else:
            napp[s[i]] = 1

            
def caesarCipher(s, k):
    # Write your code here
    new_str = ''
    for _ in range(len(s)):
        if 65 <= ord(s[_]):
            if ord(s[_]) <= 90:
                new_str += chr((ord(s[_]) + k-65)%26+65)
        if 97 <= ord(s[_]):
            if ord(s[_]) <= 122:
                new_str += chr((ord(s[_])+k-97)%26+97)
        if ord(s[_]) <64  or ord(s[_])>90 and ord(s[_])<97 or ord(s[_])>122:
            new_str += s[_]
    return new_str

# Balanced Parenthesis
def balancedParenthesis(s):
    stack = []
    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if not stack:
                return False
            char = stack.pop()
            if i == ')':
                if char != '(':
                    return False
            if i == '}':
                if char != '{':
                    return False
            if i == ']':
                if char != '[':
                    return False
    return True

expr = "{[()}]"
# print(balancedParenthesis(expr))
