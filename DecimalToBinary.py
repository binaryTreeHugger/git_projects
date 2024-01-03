
def decToBin(n):
    def maxExp(n):
        count = 0
        while n > 1:
            n //= 2
            count += 1
        return count
    
    gcd = maxExp(n)
    length = gcd + 1
    res = ''
    for i in range(length):
        if ((n - 2**(gcd - i))>= 0):
            n -= 2**(gcd - i)
            res += '1'
        else:
            res += '0'
    return res


def binToDec(n):
    res = 0; j = 0
    for i in range(len(n)-1,-1,-1):
        res += int(n[i])*2**(j)
        j += 1
    return res
        


print(decToBin(63))
print(binToDec('111111'))
