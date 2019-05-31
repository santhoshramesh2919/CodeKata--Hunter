n=input()
li=[]
for i in range(1,len(n)):
  if n[i-1]==n[i]:
    li.append(int(n[:i]+n[i+1:]))
print(max(li))

