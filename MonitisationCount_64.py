n=int(input())
li=[1000,500,100,50,10,1]
t=0
for i in li:
  while n//i>0:
    t+=n//i
    n=n%i
print(t)
