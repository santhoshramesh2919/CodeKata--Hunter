n=int(input())
li=[]
s=0
for i in range(n):
  li.append(list(map(int,input().split())))
for i in li:
  s+=sum(i)
print("{0:2f}".format((s/(n*n))))
