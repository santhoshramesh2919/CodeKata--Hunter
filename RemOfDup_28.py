s=input()
re=[]
for i in range(len(s)):
  if s[i] not in re:
    re.append(s[i])
print("".join(re))
