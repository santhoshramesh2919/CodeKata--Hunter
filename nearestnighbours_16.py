n,k=map(int,input().split(" "))
li=list(map(int,input().split()))
dic={}
op=[]
li.pop(li.index(k))
for i in li:
  dic[str(i)]=abs(i-k)
d = sorted((value, key) for (key,value) in dic.items())
for i in d:
  op.append(i[1])
for i in range(0,3):
  if i==2:
    print(op[2])
  else:
    print(op[i],end=" ")
