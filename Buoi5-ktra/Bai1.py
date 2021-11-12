a = input()
b = input()
dem = 0
for i in range(len(b)-1):
    for j in range(i,len(b)):
        if a==b[i:j+1]:
            dem+=1
            break
print(dem)