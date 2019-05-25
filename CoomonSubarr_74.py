#SAmw 
s1=input()
s2=input()
op=[]
for i in range(len(s1)-1):
  for j in range(i+1,len(s1)):
    subarr=s1[i:j+1]
    if subarr in s2:
      op.append(subarr)
print(max(op,key=len))
