# Get factors of numbers and add

def addFactors(n):
    factors = []
    for i in range(1,n-1):
        if n % i == 0:
            factors.append(i)
    print(sum(factors))

addFactors(10)
