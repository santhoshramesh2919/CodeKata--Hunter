n,k=map(int,input().split())
li=[]
op=[]
for i in range(n):
  li.append(list(map(int,input().split())))
for i in range(k):
  if li[0][i] in li[1]:
    op.append(li[0][i])

for i in range(2,n):
  res=[]
  for j in range(len(op)):
    if op[j] in  li[i]:
      res.append(op[j])
  op=res
op=set(op)
print(*op)
