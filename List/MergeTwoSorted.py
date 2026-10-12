
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4,5, 6]

l3 = []

m = len(l1)
n = len(l2)

first = 0
second = 0

while first < m and second < n:
    if l1[first] < l2[second]:
        l3.append(l1[first])
        first += 1
    else:
        l3.append(l2[second])
        second += 1

while first < m:
    l3.append(l1[first])
    first += 1

while second < n:
    l3.append(l2[second])
    second += 1

print(l3)
