def palindrome(st):
  if st==st[::-1]:
    return True
  else:
    return False
s=input()
for i in range(1,len(s)):
  if palindrome(s[::i]+s[i+1:]):
      f=1
      break
  else:
    f=0
if f==1:
  print("YES")
else:
  print("NO")
