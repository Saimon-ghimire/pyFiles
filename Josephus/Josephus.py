def m_code(num):
    n = 0
    while True:
        n = n+1
        if (2**n) <= num < (2**(n+1)):
            break
    survivor = 1+2*(num+(2**n)-(2**(n+1)))
    return(survivor)

m_code('input the number of people')

# 2 to the power n is the highest power of n you can get before exceeding the given number.
# So alternatively w(n) = 1+2(v+l-u)
# l=2^n  u=2^n+1
# Final: w(n)=1+2(v-2^n)

# This one works just upto 100 numbers.
# num=int(input("Number: "))
# n=0
# while True:
#    n=n+1
#    if (2**n)>num:
#       n=n-1
#       break
# survivor=1+2*(num-(2**n))
# print(survivor)
