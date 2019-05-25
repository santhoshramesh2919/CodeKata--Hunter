n=int(input())
li=list(map(int,input().split()))
m=0
for i in range(len(li)):
  for j in range(len(li)):
    t=abs(li[i]-li[j])
    if t>m:
      m=t
print(m)
