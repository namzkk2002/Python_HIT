a = input()
a = a.replace("‘",'')
a = a.replace("’",'')
a = a.replace(',','')
b = []
for i in range(0,len(a)):
  if int(a[i])%2==0:
    b.append(int(a[i]))
for i in range(0,len(a)):
  if int(a[i])%2!=0:
    b.append(int(a[i]))
print(b)