
def add(arr,k):
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      if arr[i]+arr[j]==k:
        return True
  else:
    return False
n,k=map(int,input().split())
li=list(map(int,input().split()))
if (add(li,k)):
  print("YES")
else:
  print("NO")
