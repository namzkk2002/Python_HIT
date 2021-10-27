str = ""
while len(str) <= 10 :
    str = input()
    if len(str) <= 10:
        print("Nhập lại")
print("Độ dài chuỗi là : ", len(str))
a = str[2:6]
print(a)
