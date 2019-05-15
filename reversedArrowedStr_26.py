n=int(input())
li=list(map(int,input().split()))
s=""
for i in range(len(li)-1,-1,-1):
  if i==0:
    s=s+str(li[i])
  else:
    s=s+str(li[i])+"->"
print(s)
