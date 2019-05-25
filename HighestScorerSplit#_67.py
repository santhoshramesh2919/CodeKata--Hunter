name1,m1,m2,m3=map(str,input().split("#"))
name2,ma1,ma2,ma3=map(str,input().split("#"))
if m1+m2+m3>ma1+ma2+ma3:
  print(name1)
else:
  print(name2)
