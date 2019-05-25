n=int(input())
li=list(map(str,input().split()))
k=input()
c=0
for i in li:
  if k==i[0:2]:
    c+=1
print(c)
