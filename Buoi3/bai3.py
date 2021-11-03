def check():
    arr1 = set(list(map(str,input("Nhập tập hợp 1 : ").split())))
    arr2 = set(list(map(str,input("NhậP tập hợp 2 : ").split())))
    if len(arr1-arr2) == 0:
        print("Tập 1 là tập con của 2")
    else:
        print("Tập 1 không phải là tập con của 2")
check()
