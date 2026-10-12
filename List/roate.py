l=[1,2,3,4,5,6]

k=2

s=l[0:2]
m=l[2::]
s.reverse()
m.reverse()
print(s)
print(m)
s.extend(m)
print(s)
s.reverse()
print(s)