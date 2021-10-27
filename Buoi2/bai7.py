from typing import Counter


n = int(input())
x = [] 
s = []
m1 = []
for i in range(n):
    a, b = input().split()
    m1.append(a)
    x.append(b)
s = []
for i in range(0,len(x)):
    s1 = "".join(x[i:i+1])
    s.append(x.count(s1))
m2=""
for i in range(0,len(s)) :
    if s[i] == max(s):
        m3 = "".join(m1[i:i+1])
        m2 = m2+m3+" ";
print(m2)
