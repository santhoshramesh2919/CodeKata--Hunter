n=input()
c=0
for i in range(0,int(n)+1):
  if i in range(0,10):
    c+=1
  else:
    f=1
    i=str(i)
    for k in range(1,len(i)):
      if (abs(int(i[k-1])-int(i[k])))==1:
        f+=1
      else:
        break
    if f==len(i):
      c+=1
print(c)
