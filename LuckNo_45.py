n=int(input())
li=list(map(int,input().split()))
n=len(li)
c=0
for i in range(1,len(li)+1):
  if n*i in li:
    c+=1
print(c)


