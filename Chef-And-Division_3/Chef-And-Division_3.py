# cook your dish here
for t in range(int(input())):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    r = sum(a)//k
    print(min(r,d))
