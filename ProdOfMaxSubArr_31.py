def prod(lis):
  res=1
  for i in lis:
    res=res*i
  return res

n=int(input())
li=list(map(int,input().split()))
m=min(li)
for i in range(len(li)-1):
  for j in range(i,len(li)):
    s=(prod(li[i:j+1]))
    if s>m:
      m=s
print(m)
