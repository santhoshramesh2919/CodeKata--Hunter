s=input()
i=0
m=0
res=""
while i<len(s)-1:
  if s[i]=='a' and s[i+1]=='b':
    res=res+s[i]+s[i+1]
    i=i+2
  else:
    res=""
    i+=1
  if m<len(res):
    m=len(res)
l=len(s)-1
if s[l]=="a" and s[l-1]=="b" and res!="":
  m=m+1
print(m)
