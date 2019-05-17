n=int(input())
li=[]
for i in range(1000000):
  e=str(i).count('3')
  f=str(i).count('4')
  if e+f==len(str(i)):
    li.append(i)
print(li,len(li),li[n-1])
