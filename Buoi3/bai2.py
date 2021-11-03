arr1 = set(list(map(str,input("Nhập tập hợp 1 : ").split())))
arr2 = set(list(map(str,input("NhậP tập hợp 2 : ").split())))
print("Các phần tử ở tập 1 nhưng không có ở tập 2 là : ",arr1 - arr2)