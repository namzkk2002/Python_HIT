import math

print("Nhập x : ")
x = float(input())
f = (x*x + math.exp(x) + math.sin(x))/(math.sqrt(x*x +1))
print("F(x) = " + str(f))