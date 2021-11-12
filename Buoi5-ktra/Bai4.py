a = input()
n = int(input())
arr = ''
for i in range(0,len(a)-1):
    s = 1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            s += 1
        else:
            arr+=str(s)+str(a[i])
            break
    i+=j
print(arr)
