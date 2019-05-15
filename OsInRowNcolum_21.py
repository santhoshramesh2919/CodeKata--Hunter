n,m=map(int,input().split())
li=[]
op=[]
for i in range(n):
  li.append(list(map(int,input().split())))
for i in range(n):
  for j in range(m):
    if li[i][j]==0:
      op.append([i,j])
for i in range(n):
  for j in range(m):
    for k in op:
      li[k[0]][j]=0
      li[i][k[1]]=0
for p in li:
  print(*p)



  
