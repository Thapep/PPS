import matplotlib.pyplot as plt
import re
serial = open('../serial/rgol.out','r')
lines = serial.readlines()

tserial = {}
l = []
for i in range(len(lines)):
    l.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    tserial[int(l[i][0])] = (float(l[i][2]))

print(tserial)   

parallel = open('./rgol.out','r')
lines = parallel.readlines()

tparallel = {}
tparallel[64] = []
tparallel[1024] = []
tparallel[4096] = []
p = []
for i in range(len(lines)):
    p.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    tparallel[int(p[i][0])].append((float(p[i][2])))
    
print(tparallel)

## Speedup 64
for k in tparallel.keys():

    if k == 64:
        sp64 = []
        for i in range(len(tparallel[k])):
            sp64.append(tserial[k]/tparallel[k][i])
            print(tserial[k])
            print(tparallel[k][i])
            print(tserial[k]/tparallel[k][i])
        print(sp64)
        plt.plot([1,2,4,6,8], sp64)
        plt.ylabel('Speedup64')
        plt.xlabel('#Processors')
        plt.show()

    if k == 1024:
        sp1024 = []
        for i in range(len(tparallel[k])):
            sp1024.append(tserial[k]/tparallel[k][i])
            print(tserial[k])
            print(tparallel[k][i])
            print(tserial[k]/tparallel[k][i])
        print(sp64)
        plt.plot([1,2,4,6,8], sp1024)
        plt.ylabel('Speedup1024')
        plt.xlabel('#Processors')
        plt.show()

    if k == 4096:
        sp4096 = []
        for i in range(len(tparallel[k])):
            sp4096.append(tserial[k]/tparallel[k][i])
            print(tserial[k])
            print(tparallel[k][i])
            print(tserial[k]/tparallel[k][i])
        print(sp4096)
        plt.plot([1,2,4,6,8], sp4096)
        plt.ylabel('Speedup4096')
        plt.xlabel('#Processors')
        plt.show()