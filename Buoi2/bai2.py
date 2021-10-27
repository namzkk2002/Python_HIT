aList = list(map(int, input().split()))
result = [0]*len(aList)
for i in range(0,len(aList)) :
    s = 0;
    for j in range(0,i+1):
        s += aList[j]
    result[i] = s
print(result)