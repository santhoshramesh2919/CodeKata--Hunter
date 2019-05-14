def isSubset(a,b):
  op=[]
  for i in range(len(b)):
    if b[i] in a:
      op.append(b[i])
  if len(op)==len(b):
    return True
  else:
    return False

n,m=map(int,input().split())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
if isSubset(li1,li2):
  print("YES")
else:
  print("NO")
