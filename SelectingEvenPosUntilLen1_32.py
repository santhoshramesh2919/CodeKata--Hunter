def selection(lis):
  res=[]
  for i in range(0,len(lis)):
    if i%2==1:
      res.append(lis[i])
  if len(res)==1:
    print(li.index(res[0]))
  else:
    selection(res)


n=int(input())
li=list(map(int,input().split()))
selection(li)
