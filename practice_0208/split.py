f = open ('pv.txt', 'r')

for i in f:
    a = i.rstrip().split()
    for j in a:
        print(j)



f.close()