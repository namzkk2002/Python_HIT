str = input("Nhập chuỗi : ");
a = str.find("T")
b = str.find("R",a , len(str))
print(b)
c = str.find("Ẻ",b,len(str))
print(c)
d = str.find("T",c,len(str))
print(d)
e = str.find("R",d,len(str))
print(e)
f = str.find("Â",e,len(str))
print(f)
g = str.find("U",f,len(str))
print(g)
if a == -1 or b == -1 or c == -1 or d == -1 or e == -1 or f == -1 or g == -1 :
    print("Không TRẺ TRÂU")
else:
    print("TRẺ TRÂU")
