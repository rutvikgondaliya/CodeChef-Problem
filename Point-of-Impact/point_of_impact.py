# cook your dish here
for t in range(int(input())):
    n,k,x,y = map(int,input().split())
    
    if x==y :
        print(n,n)
    else:
        p = []
        if x < y :
            p = [[n+x-y,n],[n,n+x-y],[y-x,0],[0,y-x]]
        else:
            p = [[n,n+y-x],[n+y-x,n],[0,x-y],[x-y,0]]
        
        t = p[(k-1)%4]
        print(t[0],t[1])
