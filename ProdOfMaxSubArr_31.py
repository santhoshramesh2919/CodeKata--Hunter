import  numpy
n=int(input())
li=list(map(int,input().split()))
m=min(li)
for i in range(len(li)-1):
  for j in range(i,len(li)):
    s=(numpy.prod(li[i:j+1]))
    if s>m:
      m=s
print(m)
