n=6
space=n-1
c=1
for i in range(n):
    print((" "*space)+('*'*c))
    c+=2
    space-=1

# if u code upto this it will  be triangle............................................

space=1
c-=4
for i in range(n-1):
    print((' '*space)+('*'*(c)))
    c-=2
    space+=1

#-----------------------------------------------------------------------------------------------------------------------------

# gcd of 2 numbers

def gcd(a,b):
    while(a!=0):
        a,b=b%a,a
    return b

def lcm(a,b):
    return a*b/gcd(a,b)

# print(gcd(12,24))
# print('%.0f'%lcm(12,18))
