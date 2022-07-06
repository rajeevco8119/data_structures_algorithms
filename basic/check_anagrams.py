# check anagrams

def checkAnagrams(str1, str2):
    sum1,sum2 = 0,0
    for i in str(str1):
        sum1 += ord(i)-ord('a')
    for i in str(str2):
        sum2 += ord(i) - ord('a')
    return sum1 == sum2

print(checkAnagrams('rajeev','vajeer')) # True
print(checkAnagrams('rajEeV','Vajeer')) # False
print(checkAnagrams('rajeeV','Vajeer')) # True
print(checkAnagrams('RAJEEV','VaJEER')) # False
print(checkAnagrams('rajev','vajeer')) # False
