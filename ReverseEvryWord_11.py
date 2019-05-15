str=list(input().split(" "))
op=[]
for i in str:
  s=""
  for j in range(len(i)):
    s=i[j]+s
  op.append(s)
print(*op)
