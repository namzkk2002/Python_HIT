str = input()
a = str.index('(')
print(" ".join(str[a+1:len(str)-1].split(",")))