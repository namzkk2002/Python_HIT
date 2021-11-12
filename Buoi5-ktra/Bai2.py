def check(x):
    '''
    :param:
    :input
        la so x
    :ouput
        tra ve 1 hoac 0
    '''
    t = 0
    for i  in range(1,x):
        if x%i==0:
            t+=i
    if t > x :
        return 1
    return 0


a = []
n = int(input())
for i in range(0,n):
    a.append(int(input()))
a.sort()
dem = 0
s = ''
for i in range(0,n):
    if check(a[i])==1:
        dem+=1
        s+=str(a[i]) + ' '
print(dem)
print(s)
