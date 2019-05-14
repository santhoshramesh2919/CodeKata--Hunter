n=int(input())
arr=list(map(int,input().split()))
dic=[]
for i in arr:
  if arr.count(i)>1:
    dic.append(i)
s=set(dic)
if len(s)==0:
  print("Unique")
else:
  print(*s)
