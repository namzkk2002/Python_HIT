def check(n):
    b = n 
    s = 0
    while b>0:
        s+=b%10;
        b=int(b/10)
    return s

x = int(input())
while x>9 :
    x=check(x)
print(x)