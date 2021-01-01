# cook your dish here
for t in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    i = 0
    j = True
    while sum(a)<=sum(b):
        a.sort()
        b.sort()
        if a[0]<b[-1]:
            temp = b[-1]
            b[-1] = a[0]
            a[0] = temp
            i += 1
        else:
            j = False
            print(-1)
            break
    if j == True:
        print(i)
