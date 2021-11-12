def check(x):
    '''
    :param:
    :input
        la so x
    :ouput
        tra ve 1 hoac 0
    '''
    t = 0
    for i  in range(1,x+1):
        if x%i==0:
            t+=1
    if t == 3 :
        return 1
    return 0

n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
dem = 0
for i in range(0,n):
    if check(a[i]) == 1:
        dem+=1
if dem==0:
    print("KHÔNG")
else:
    print(dem)
