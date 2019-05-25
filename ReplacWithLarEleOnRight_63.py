n=int(input())
li=list(map(int,input().split()))
op=[]
for i in range(0,len(li)-1):
  op.append(max(li[i+1:]))
op.append(0)
print(*op)
