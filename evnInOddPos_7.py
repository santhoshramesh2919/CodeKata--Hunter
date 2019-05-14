n=int(input())
arr=list(map(int,input().split()))
op=[]
for i in range(len(arr)):
  if arr[i]%2==0 and i%2==1:
    op.append(arr[i])
  elif arr[i]%2==1 and i%2==0:
    op.append(arr[i])
for i in range(0,len(op)):
  if(i==len(op)-1):
    print(op[i])
  else:
    print(op[i],end=" ")
