#Minimum value
def func(li):
  min=[]
  for i in range(0,len(li)-1):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==0:
          print(li[i],li[j])
          return
        elif min==[]:
          min=[li[i],li[j]]
        else:
          if li[i]+li[j]<sum(min):
            min=[li[i],li[j]]
  print(*min)
  return
n=int(input())
li=list(map(int,input().split()))
func(li)

