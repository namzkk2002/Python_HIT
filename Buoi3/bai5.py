def MyMathShower(*arr): 
    t = 0.0
    s = 1.0
    h = 2.0*arr[0]
    for n in arr:
        t+=n
        s*=n
        h-=n
    print(t,s,h)
MyMathShower(10,4,1,1)
    
