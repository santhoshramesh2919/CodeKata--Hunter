s=input()
subst=""
f=0
for i in range(len(s)-1):
  subst=s[:i+1]
  if subst!=subst[::-1]:
    op=subst
    f=1
  else:
    f=0
  
if(f==1):
  print(op)
else:
  print(s)
