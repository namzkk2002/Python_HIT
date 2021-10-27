a = input()
b = a.count('1')
c = 0
if b%2==0:
    for i in range(len(a)) :
        if a[i]=='1':
            c+=1
        if c==b/2:
            c=i+1;
            break
    print(a[:c]+" "+a[c:])
else:
    print("NO")