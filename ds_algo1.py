 # Find missing number
 a = [1,3,4,2,6,7,9,5,10,13,11,12]

 def af(a):
     sum = 0
     for i in range(len(a)):
         sum += int(a[i])
     b = len(a)
     c = ((b+2)*(b+1))/2
     return c-sum
 print(af(a))

 # Determine if sum is equal to 2 values
 def bf(a,trget):
     i = 0
     a.sort()
     # print(a)
     c = len(a)-1
     # print(a)
     # print(a[c])
     while i < c:
         sum = a[i]+a[c-1]
         # print(str(sum)+"fi"+str(a[i])+"se"+str(a[c-1]))
         if trget == sum:
             print(str(a[i])+" "+str(a[c-1]))
             i = i+1
         elif trget > sum:
             i = i+1
         else:
             c = c-1

     return "Nil"

 def cf(a,sum):
     s = set()
     for i in range(len(a)):
         temp = sum - a[i]
         if temp in s :
             print(str(temp) + " "+ str(a[i]))
         s.add(a[i])

 a = [1,3,4,2,6,7,9,5,10,13,11,12]
 target = 25
 cf(a,target)

 N = 0
 E = 1
 S = 2
 W = 3

 def isCircular(path):
     x = 0
     y = 0
     dir = N
     for i in range(len(path)):
         move = path[i]
         if move == 'R':
             dir = (dir+1)%4
         elif move == 'L':
             dir = (4 + dir - 1) % 4
         else:
             if dir == 'N':
                 y += 1
             elif dir == 'E':
                 x += 1
             elif dir == 'S':
                 y -= 1
             else:
                 x -= 1
     return (x == 0 and y == 0)

 def df(arr):
     dep = 0
     minDep = 0
     for i in arr:
         if i=='(':
             dep += 1
         else:
             dep -= 1
         if minDep > dep:
             minDep = dep
     if minDep < 0:
         for i in range(abs(minDep)):
             arr = '('+ arr
     dep = 0
     for i in arr:
         if (i == '('):
             dep += 1
         else:
             dep -= 1
     if (dep != 0):
         for i in range(dep):
             arr = arr + ')'

     return arr

 Str = ")))()"
 print(df(Str))


 def count_occurence(arr,temp):
     count = {}
     count[temp] = 0
     for i in arr:
         if i == temp:
             count[temp] += 1
     return count[temp]

 def all_frequency(arr):
     count = {}
     for i in arr:
         if i in count:
             count[i] += 1
         else:
             count[i] = 1
     return count
 str= "geeksforgeeks"
 c = 'e'
 print(count_occurence(str,c))
 print(all_frequency(str))

 a = map(int,input().split())

 str1 = 'aaabbbbccdebbbbb'


 def listToString(s):
     # initialize an empty string
     str1 = ""

     # traverse in the string
     for ele in s:
         str1 += ele

         # return string
     return str1
 import json


 def str_count(arr):
     count = {}
     strA = ''
     c = []
     for i in arr:
         if i in count:
             count[i] += 1
         else:
             count[i] = 1
     for k,v in count.items():
         c.append(str(k))
         c.append(str(v))
     # c = str(c)
     for i in c:
         strA += i
     print(strA)
 str_count(str1)

 def str_count(arr):
     count = {}
     count[arr[0]] = 1
     a = arr[0]
     for i in arr[1:]:
         if i == a:
             count += 1

# FCTRL2
 t = int(input())
 while t:
     prod = 1
     a = int(input())
     for i in range(1,a+1):
         prod *= i
     print(prod)

 t = int(input())
 winner = 0
 max = 0
 while t:
     a,b = map(int,input().split())
     max = abs(a - b)
     winner = 0
     if a>b:
         if a-b > max:
             max = a-b
             winner = 1
     elif a<b:
         if b-a > max:
             max = b-a
             winner = 2
     t = t-1

 print(winner)
 print(max)

# FLOW007
 t = int(input())
 while t:
     sum = 0
     a = int(input())
     while a > 0:
         b = a%10
         sum = 10*sum+b
         a = int(a/10)
     print(sum)
     t = t-1

# FLOW013
 t = int(input())
 while t:
     a,b,c = map(int,input().split())
     if a+b+c == 180:
         print('YES')
     else:
         print('NO')
     t = t-1

 # CHEFSQ
 t = int(input())
 flag = 0
 while t:
     a = int(input())
     b = list(map(int,input().split()))
     d = int(input())
     c = list(map(int,input().split()))
     i =  0
     j = 0
     while i < a and j < d:
         if c[j] == b[i]:
             i += 1
             j += 1
         else:
             i += 1
     if j == d:
         print('YES')
     else:
         print('NO')
     t = t-1

 # CHEFSQ
 t = int(input())
 flag = 0
 while t:
     a = int(input())
     b = list(map(int,input().split()))
     d = int(input())
     c = list(map(int,input().split()))
     s = []
     # If intersection of b and c is equal to length of c , then print YES else NO
     for i in c:
         if i in b:
           s.append(i)
     if len(s) == d:
         print('YES')
     else:
         print('NO')
     t = t-1

 #LOSTMAX
 for _ in range(int(input())):
     a = list(map(int,input().split()))
     b = len(a)-1
     a.remove(b)
     print(max(a))

# BIT2A
 for _ in range(int(input())):
     b = int(input())
     c = ''
     a = list(map(int,input().split()))
     for i in range(b):
         count = 0
         for j in range(i+1,b):
             if a[j]>a[i]:
                 count += 1
         a[i] = count
         c = [str(i) for i in a]
         c = ''.join(c)
     print(c)

# SUMPOS
 for _ in range(int(input())):
     a = list(map(int,input().split()))
     sum = 0
     for i in range(len(a)):
        sum += a[i]
     b = int(sum)/2
     if b in a:
         print("YES")
     else:
         print('NO')

# RAINBOWA
 for _ in range(int(input())):
     a = list(map(int,input().split()))
     pass

# FSQRT
import math
for _ in range(int(input())):
     a = int(input())
     b = int(math.sqrt(a))
     print(b)

# CIELRCPT
 for _ in range(int(input())):
     a = int(input())
     menu = [2**i for i in range(11,-1,-1)]
     count = 0
     for p in menu:
         while a >= p:
             a -= p
             count += 1
     print(count)

# FLOW005
 for _ in range(int(input())):
     a = int(input())
     lst = [100,50,10,5,2,1]
     count = 0
     for l in lst:
         while a >= l:
             a -= l
             count += 1
     print(count)

# PALL01
 for _ in range(int(input())):
     a = str(input())
     l = 0
     r = len(a)-1
     flag = 0
     while l<r:
         if a[l] != a[r]:
             print('loses')
             flag = 1
             break
         l += 1
         r -= 1
     if flag == 0:
         print('wins')

# FLOW010
 for _ in range(int(input())):
   a = str(input())
   mapping = {'B':'Battleship','b':'Battleship','C':'Cruiser','c':'Cruiser','D':'Destroyer','d':'Destroyer','F':'Frigate','f':'Frigate'}
   print(mapping[a])

# MATCHES
 for _ in range(int(input())):
     mapping = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
     c = 0
     for i in str(sum(list(map(int, input().split())))):
         c += mapping[i]
     print(c)

 for _ in range(int(input())):
     a = list(map(int, input().split()))

 # Substrings of a string (2 at a time)
 def substring(arr):
     s = []
     for i in range(len(arr)):
         for j in range(i,len(arr)):
             s.append(arr[i]+arr[j])
     print(s)
 str1 = 'rajiv'
 substring(str1)
 O/P = ['rr', 'ra', 'rj', 'ri', 'rv', 'aa', 'aj', 'ai', 'av', 'jj', 'ji', 'jv', 'ii', 'iv', 'vv']

# Substring of a string
 def substring2(arr):
     for i in range(0,len(arr)):
         for j in range(i+1,len(arr)+1):
             print(arr[i:j])

 str1 = 'rajiv'
 substring2(str1)

 # Permutations
 def permute(arr):
     l = []
     for i in range(len(arr)):
         for j in range(i+1,len(arr)):
             x = arr[i]
             rem = arr[:i]+arr[i+1:]
             l.append(x+rem)
             l.append(rem+x)
     print(l)

 def permute(arr):
     l = []
     for i in range(0,len(arr)):
         x = arr[i]
         rem = arr[:i]+arr[i+1:]
         l.append(x+rem)
         l.append(rem+x)
     print(l)

 arr = '123'
 permute(arr)

 # HOWMANY
 a = int(input())
 if a/10 < 1:
     print(1)
 elif (a/100 < 1 and a/10 >= 1):
     print(2)
 elif (a/1000 <1 and a/100 >= 1):
     print(3)
 else:
     print('More than 3 digits')

 # Most frequent elements
 def mf(arr):
     count = {}
     res = 0
     max_count = -1
     for i in range(len(arr)):
         if arr[i] not in count:
             count[arr[i]] =1
         else:
             count[arr[i]] += 1
     max_count = 0
     res = -1
     for i in count:
         if (max_count < count[i]):
             res = i
             max_count = count[i]

     return res
 arr = [1, 5, 2, 1, 3, 2, 1]

 print(mf(arr))

 # Symmetric Pairs
 def sp(arr):
     hm = dict()
     for i in range(len(arr)):
         x = arr[0][i]
         y = arr[1][i]

         if y in hm.keys() and hm[y]==x:
             print(x+""+y)
         else:
             hm[x] = y

 # Smallest unsorted subarray
 def shortestUnsortedSubarray(arr):
     i = 0
     j = len(arr)-1
     count = 0
     while i<j:
         count = count + 1
         if count > len(arr):
             break
         if arr[i+1] > arr[i]:
             i = i+1
         if arr[j-1] < arr[j]:
             j = j-1

     print("Index from "+str(i+1)+" to "+str(j-1))
     for a in range(i+1,j):
         print(arr[a])

 arr2 = [10, 12, 20, 30, 35, 29, 32, 39, 35, 50, 60]
 arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
 shortestUnsortedSubarray(arr2)

# SMPAIR
 for _ in range(int(input())):
     a = int(input())
     b = list(map(int,input().split()))
     b.sort()
     print(b[0]+b[1])

# TWOVSTEN
 for _ in range(int(input())):
     x = int(input())
   # if x%10==0:
   #     print(0)
   # else:
   #     y = x*2
   #     if y %10 == 0:
   #         print(1)
   #     else:
   #         print(-1)

# GDOG
 T = int(input())
 for i in range(T):
     N, K = map(int, input().split())
     m = 0
     g = K
     while g > m:
         m = max(m, N % g)
         g -= 1
     print(m)

# RECTANGL
 for _ in range(int(input())):
     a,b,c,d = map(int,input().split())
     if a==b and c==d or a==c and b==d or a==d and b==c:
         print('YES')
     else:
         print('NO')

# Find the sum of digits of a number at even and odd places
#  Input: N = 54873
#  Output:
#  Sum odd = 16
#  Sum even = 11
# 
#  Input: N = 457892
#  Output:
#  Sum odd = 20
#  Sum even = 15
 def sum_even_odd(number):
     sum_e = 0
     sum_o = 0
     flag = 0
     while number > 0:
         number = int(number)
         if flag == 0:
             a = (number%10)
             sum_o += int(a)
             flag = 1
         else:
             sum_e += (number%10)
             flag = 0
         number /= 10
     print(sum_o)
     print(sum_e)
 sum_even_odd(54873)
 sum_even_odd(457892)

 # Length of longest Subarray with equal number of odd and even elements
 # Given an integer array arr[], the task is to find the length of the longest subarray with an equal number of odd and even elements.
 # Input: arr[] = {1, 2, 1, 2}
 # Output: 4
 # Explanation:
 # Subarrays in the given array are –
 # {{1}, {1, 2}, {1, 2, 1}, {1, 2, 1, 2}, {2}, {2, 1}, {2, 1, 2}, {1}, {1, 2}, {2}}
 # where the length of the longest subarray with an equal number of even and odd elements is 4 – {1, 2, 1, 2}
 # Input: arr[] = {12, 4, 7, 8, 9, 2, 11, 0, 2, 13}
 # Output: 8


 # Find max length subarray having a given sum
 def findMaxLengthSub(arr, k):
     maxL = 0
     ending_index = 0
     for i in range(len(arr)):
         sum = 0
         for j in range(i,len(arr)):
             sum += arr[j]
             if sum == k:
                 if maxL < j-i+1:
                     maxL = j-i+1
                     ending_index = j
     print(ending_index-maxL+1, ending_index)
 A = [5, 6, -5, 5, 3, 5, 3, -2, 0]
 sum = 8
 findMaxLengthSub(A,sum)
         # ^  (Problems are linked)
         # |
         # |
         # |
         # |
         # V
 def longest_sub(arr):
     b = []
     for i in arr:
         if i % 2 ==0:
             b.append(1)
         else:
             b.append(-1)
     # Problem reduces to finding sum zero with max length
     findMaxLengthSub(b,0)
 B = [12, 4, 7, 8, 9, 2, 11, 0, 2, 13]
 longest_sub(B)

 import random

 def randomize(arr,n):
     for i in range(len(arr)-1,0,-1):
         j = random.randint(0,i+1)
         arr[i],arr[j] = arr[j],arr[i]
     print(arr)

 arr = [1, 2, 3, 4, 5, 6, 7, 8]
 n = len(arr)
 randomize(arr, n)

 # Longest common substring
 def lcs(st1,st2,m,n):
     if m == 0 or n ==0:
         return 0
     elif st1[m-1]==st2[n-1]:
         return 1+lcs(st1,st2,m-1,n-1)
     else:
         return max(lcs(st1,st2,m-1,n),lcs(st1,st2,m,n-1))

 X = "AGGTAB"
 Y = "GXTXAYB"
 print("Length of LCS is ", lcs(X , Y, len(X), len(Y)))

 # Find all possible substrings after deleting k characters
 # Input : geeks, k = 1
 # Output : {'gees', 'eeks', 'geks', 'geek'}
 # 
 # Input : dog, k = 1
 # Output : {'do', 'dg', 'og'}

 def one_less_substring(st,k):
     lst = []
     for i in range(-1,len(st)-k):
         print(st[:i+k]+st[i+k+1:])

 str4 = 'dog'
 str5 = 'rajiv'
 one_less_substring(str5,1)

 def k_less_substring(st,k):
     lst = []
     for i in range(0,len(st)):
         print(st[:i]+st[i+k:])

 str4 = 'dog'
 str5 = 'rajiv'
 k_less_substring(str5,2)


 def one_less_substring(st,k):
     lst = []
     for i in range(-1,len(st)-k):
         print(st[:i+k]+st[i+k+1:])

 # str4 = 'dog'
 str5 = 'rajiv'
 one_less_substring(str5,1)

 # Query Range MO Decomposition
 def queryRange(arr,Q):
     for i in Q:
         sum = 0
         p, q = i
         for j in range(p,q+1):
             sum += arr[j]
         print(sum)

 arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
 Q = [[0, 4], [1, 3], [2, 4]]
 queryRange(arr,Q)


 # No of ways to traverse matrix
 def count(m,n):
     if m == 1 or n == 1:
         return 1
     return count(m-1,n)+count(m,n-1)

 print(count(5,5))

 # All sublists of a list in python
 Input  : list = [1, 2, 3]
 Output : [[], [1], [1, 2], [1, 2, 3], [2],
          [2, 3], [3]]

 Input : [1, 2, 3, 4]
 Output : [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4],
          [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]

 def subset(arr):
     lists = [[]]
     for i in range(len(arr)+1):
         for j in range(i):
             lists.append(arr[j:i])
     print(lists)

 l1 = [1, 2, 3]
 print(subset(l1))

# PPSUM
 def sum(a):
     return (a*(a+1))/2

 for _ in range(int(input())):
     a,b = map(int,input().split())
     result = sum(b)
     while a-1 > 0:
         result = sum(result)
         a -= 1
     print(int(result))


# FLOW016
 # cook your dish here
 def gcd(a, b):
     if a == 0:
         return b
     elif b == 0:
         return a
     elif a == b:
         return a
     elif (a > b):
         return gcd(a - b, b)
     else:
         return gcd(a, b - a)


 for _ in range(int(input())):
     a, b = map(int, input().split())
     GCD = int(gcd(a, b))
     LCM = a * b
     LCM /= GCD
     LCM = int(LCM)
     print(str(GCD) + " " + str(LCM))

# ICM0013
 for _ in range(int(input())):
     res = 0
     a = int(input())
     for i in range(a):
         if i % a <= int(a/2)+1:
             res += 1
     print(res)

 # Given a string, find the first non repeating character.
 def firstChar(arr):
     count = {}
     keys = []
     values = []
     for i in arr:
         if i in count:
             count[i] += 1
         else:
             count[i] = 1
     for k,v in count.items():
         keys.append(k)
         values.append(v)
     for j in range(len(keys)):
         if values[j] == 1:
             print(keys[j])
             break
 s= 'geeksforgeeks'
 firstChar(s)

 # Given an array, find the number of contiguous subarrays such that the product of the elements of the subarray is less than or equal to a given positive integer k.
 def funcarray(arr,k):
     count = 0
     for i in range(len(arr)):
         j = arr[i]
         if j <= k:
             count += 1
         for l in range(i+1,len(arr)):
             j *= arr[l]
             if j <= k:
                 count += 1
             else:
                 break
     print(count)


 arr = [1,2,3,4]
 funcarray(arr,10)

 # Window Sliding Technique
 # Given an array of integers of size ‘n’.
 # Our aim is to calculate the maximum sum of ‘k’
 # consecutive elements in the array.
 # 
 # Input  : arr[] = {100, 200, 300, 400}
 #          k = 2
 # Output : 700
 # 
 # Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
 #          k = 4
 # Output : 39
 # We get maximum sum by adding subarray {4, 2, 10, 23}
 # of size 4.
 # 
 # Input  : arr[] = {2, 3}
 #          k = 3
 # Output : Invalid
 # There is no subarray of size 3 as size of whole
 # array is 2.

 def sliding_windows(arr,k):
     sum = 0
     max_sum = 0
     for i in range(0,len(arr)-k+1):
         sum = 0
         for j in range(0,k):
             sum += arr[i+j]
         max_sum = max(max_sum,sum)
     print(max_sum)

 arr = [1, 4, 2, 10, 2,
        3, 1, 0, 20]
 k = 4
 sliding_windows(arr,k)

 # Total decoding messages
 # Input:  digits[] = "121"
 # Output: 3
 # // The possible decodings are "ABA", "AU", "LA"
 # 
 # Input: digits[] = "1234"
 # Output: 3
 # // The possible decodings are "ABCD", "LCD", "AWD"

 def helper(arr):
     if len(arr) == 0 or (len(arr)==1 and arr[0]=='0'):
         return 0
     return decode(arr,len(arr))
 def decode(arr,n):
     if n == 0 or n == 1:
         return 1
     count = 0
     if arr[n-1] >= "0":
         count = decode(arr,n-1)
     if arr[n-2] == '1' or (arr[n-2] == '2' and arr[n-1] < '7'):
         count += decode(arr,n-2)
     return count
 digits = "1234"
 print(helper(digits))

 # Non-overlapping sum of two sets
 def non_overlap(a,b):
     sum = 0
     m = len(a)
     n = len(b)
     for i in a:
         if i in b:
             continue
         else:
             sum += i
     for i in b:
         if i in a:
             continue
         else:
             sum += i
     print(sum)


 A = [5, 4, 9, 2, 3]
 B = [2, 8, 7, 6, 3]
 non_overlap(A,B)

 # Largest subarray with equal number of 0s and 1s
 def maxLen(arr,n):
     hash_map = {}
     curr_sum = 0
     max_len = 0
     ending_index = -1
     for i in range(0,n):
         if arr[i]==0:
             arr[i] = -1
         else:
             arr[i] = 1

     for i in range(0,n):
         curr_sum += arr[i]
         if curr_sum == 0:
             max_len = i+1
             ending_index = i
         if curr_sum in hash_map:
             if  max_len < i - hash_map[curr_sum]:
                 max_len = i-hash_map[curr_sum]
                 ending_index = i
         else:
             hash_map[curr_sum] = i
     for i in range(0, n):
         if (arr[i] == -1):
             arr[i] = 0
         else:
             arr[i] = 1
     print(ending_index - max_len + 1, end=" ")
     print("to", end=" ")
     print(ending_index)

     return max_len


 # A triplets that sum up to a given value
 def triplet_sum1(arr,sum):
     for i in range(0,len(arr)-2):
         for j in range(i+1,len(arr)-1):
             for k in range(j+1,len(arr)):
                 if arr[i]+arr[j]+arr[k] == sum:
                     print(str(arr[i])+" "+str(arr[j])+" "+str(arr[k]))
                     break

 def triplet_sum2(arr,sum):
     arr.sort()

     for i in range(0, len(arr) - 2):
         l = i + 1
         r = len(arr) - 1
         while (l < r):

             if (arr[i] + arr[l] + arr[r] == sum):
                 print("Triplet is",arr[i],
                       ', ', arr[l], ', ', arr[r])
                 return True

             elif (arr[i] + arr[l] + arr[r] < sum):
                 l += 1
             else:  # A[i] + A[l] + A[r] > sum
                 r -= 1
     return False

 def triplet_sum3(arr,sum):
     s = set()
     for i in range(len(arr)-1):
         curr = sum-arr[i]
         for j in range(i+1,len(arr)):
             if curr-arr[j] in s:
                 print("Triplet is", arr[i],
                       ", ", arr[j], ", ", curr - arr[j])
                 return True
             s.add(arr[j])
     return False

 A = [1, 4, 45, 6, 10, 8]
 sum = 22
 triplet_sum1(A,sum)
 triplet_sum2(A,sum)
 triplet_sum3(A,sum)


 # Count pairs whose products exist in array
 def pairExists(arr,prod):
     s = set()
     count = 0
     for i in arr:
         s.add(i)
     for i in range(len(arr)-1):
         for j in range(i+1,len(arr)):
             if arr[i]*arr[j] == prod:
                 count += 1
     print(count)
 arr = [6, 2, 4, 12, 5, 3]
 pairExists(arr,12)

 # 2D Matrices
 # 
 # Traversal
 def traversal2D(arr):
     for i in range(len(arr)):
         for j in range(len(arr[i])):
             print("i="+str(i)+", j="+str(j)+"  "+str(arr[i][j]))

 mat = [[12, 1, 14, 3, 16],
        [14, 2, 1, 3, 35],
        [14, 1, 14, 3, 11],
        [14, 25, 3, 2, 1],
        [1, 18, 3, 21, 14]]
 traversal2D(mat)

 # Find distinct elements common to all rows of a matrix
 def commonElements(arr):
     n = len(arr)
     hash = {}
     for i in range(len(arr)):
         hash[arr[0][i]] = 1

     for i in range(1,n):
         temp = {}
         for j in range(n):
             temp[arr[i][j]] = 1
         for itr in list(hash):
             if itr not in temp:
                 del hash[itr]
         if len(hash) == 0:
             break
     for i in list(hash):
         print(i,end=" ")


 def sortRows(arr):
     for i in range(len(arr)):
         arr[i].sort()
     print(arr)

 def print2D(arr):
     for i in range(len(arr)):
         for j in range(len(arr[i])):
             print(arr[i][j])

 mat = [[12, 1, 14, 3, 16],
        [14, 2, 1, 3, 35],
        [14, 1, 14, 3, 11],
        [14, 25, 3, 2, 1],
        [1, 18, 3, 21, 14]]
 sortRows(mat)
 commonElements(mat)

 # Rotate a Matrix by 180 degree
 # Input :  1  2  3
 #          4  5  6
 #          7  8  9
 # Output : 9 8 7
 #          6 5 4
 #          3 2 1
 # 
 # Input :  1 2 3 4
 #          5 6 7 8
 #          9 0 1 2
 #          3 4 5 6
 # Output : 6 5 4 3
 #          2 1 0 9
 #          8 7 6 5
 #          4 3 2 1

 def rotate180(arr):
     n = len(arr)
     for i in range(len(arr)-1,-1,-1):
         for j in range(len(arr[i])-1,-1,-1):
             print(arr[i][j],end=" ")
         print()

 mat = [[1, 2, 3],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]]
 rotate180(mat)

 # Rotate a matrix by 90 degree
 # Input:
 #  1  2  3
 #  4  5  6
 #  7  8  9
 # Output:
 #  3  6  9
 #  2  5  8
 #  1  4  7
 # 
 # Input:
 #  1  2  3  4
 #  5  6  7  8
 #  9 10 11 12
 # 13 14 15 16
 # Output:
 #  4  8 12 16
 #  3  7 11 15
 #  2  6 10 14
 #  1  5  9 13


 def rotate90(arr):
     n = len(arr)
     for i in range(len(arr)):
         for j in range(len(arr[0])):
             print(arr[j][n-i-1],end=" ")
         print()
 mat = [[1, 2, 3],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]]
 mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]
 rotate90(mat2)


