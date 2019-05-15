n=int(input())
li=list(map(int,input().split()))
st=[]
spst=[]
for i in range(len(li)):
  if i==len(li)-1:
    st.append(li[i])
  else:
    for j in range(i+1,len(li)):
      if li[i]<=li[j]:
        break
    else:
      st.append(li[i])
print(*st)
print(max(li))
