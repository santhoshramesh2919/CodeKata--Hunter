m,n=map(int,input().split())
li=list(map(int,input().split()))
li1=li[:m]
li2=li[m:]
op=[]
for i in li1:
  if i in li2:
    op.append(i)
print(*set(sorted(op)))
