w,s=input().split()
w=int(w)
s=int(s)
if (s<0)or(w<0):
    q=0
elif (s<250):
    q=w*s
elif (s<500):
    q=w*s*0.98
elif (s<1000):
    q=w*s*0.95
elif (s<2000):
    q=w*s*0.92
elif (s<3000):
    q=w*s*0.9
else:
    q=w*s*0.85
print(int(q))