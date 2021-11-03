def xd10(x):
    for i in x:
        if i=='0'or i=='1':
            return True
    return False
def ss10(x , y):
    set1 = {""}
    set2 = {""}
    for i in range(len(x)):
        if x[i]=='0'or x[i]=='1':
            set1.add(i)
    for i in range(len(y)):
        if y[i]=='0'or y[i]=='1':
            set2.add(i)
    if len(set1-set2)==0 and len(set2-set1)==0:
        return True
    else:
        return False
arr = list(map(str, input().split()))
arr2 = []
for i in range(len(arr)):
    if xd10(arr[i]) == True:
        arr2.append(arr[i])
for i in range(len(arr2)):
    for j in range(i+1,len(arr2)):
        if ss10(arr2[i],arr2[j])==True:
            arr2.remove(arr2[j])
print(arr2)








