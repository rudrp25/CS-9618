b = [[1,2,3],[4,5,6]]
for i in range(0,2):
    print(b[i])

c = [[]]
for i in range(1,4):
    c.append([i])
    print(c[i])


list  = [[0]*3 for i in range(3)]
for i in range(len(list)):
    print(list[i])
