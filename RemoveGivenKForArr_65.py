n,k=map(int,input().split())
li=list(map(int,input().split()))
res=[]
for i in li:
  if i!=k:
    res.append(i)
if len(res)>0:
  print(*res)
else:
  print("empty")
