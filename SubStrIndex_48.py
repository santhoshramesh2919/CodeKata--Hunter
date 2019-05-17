def substr(s1,s2):
  for i in range(len(s1)-1):
    for j in range(i+1,len(s1)):
      if s1[i:j+1]==s2:
        return i
      
  else:
    return -1

a=input()
b=input()
print(substr(a,b))
