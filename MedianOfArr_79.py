import math

n=int(input())
li=list(map(int,input().split()))
while(n!=0):
  if n%2==1:
    print(li[n//2])
    li.pop(n//2)
    n=n-1
  elif n%2==0:
    print(math.floor((li[n//2-1]+li[n//2])/2))
    li.pop(n//2-1)
    li.pop(n//2-1)
    n=n-2


