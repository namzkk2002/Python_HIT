a = list(map(int, input("Nhập mảng a : ").split()))
k = int(input("Nhập k : "))
dem = 0;
for  i in range(0,len(a)-1):
    for j in range(i+1,len(a)) :
        if a[i]+a[j]==k :
            dem+=1
print(dem)
