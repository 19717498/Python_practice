lst = [1,2,3,4,2,3,4,6,7,8,2,7,8]


d = {}

for i in lst:
    if i in d:
        d[i] +=1

    else:
        d[i] = 1


print(d)