n,k=map(int,input().split())
i=0
result=0
while n!=0:
    n-=1
    i+=1
    if i==k:
        i=0
        n+=1
    result+=1
print(result)