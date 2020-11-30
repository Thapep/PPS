import matplotlib.pyplot as plt
import re
import numpy as np
serial = open('../serial/rgol.out','r')
lines = serial.readlines()

tserial = {}
l = []
for i in range(len(lines)):
    l.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    tserial[int(l[i][0])] = (float(l[i][2])) 

parallel = open('./rgol1.out','r')
lines = parallel.readlines()

tparallel = {}
tparallel[64] = []
tparallel[1024] = []
tparallel[4096] = []
p = []
for i in range(len(lines)):
    p.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    tparallel[int(p[i][0])].append((float(p[i][2])))

for k in tparallel.keys():

    if k == 64:
        sp64 = []
        for i in range(len(tparallel[k])):
            sp64.append(tserial[k]/tparallel[k][i])
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 5, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylabel("time (ms)")
        plt.plot(tparallel[k], label="Time", color="blue", marker='x')
        plt.title("Game of Life in 64×64 table")
        plt.savefig("time_64.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 5, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylabel("speedup")
        plt.plot(sp64, label="Speedup", color="blue", marker='x')
        plt.title("Game of Life in 64×64 table")
        plt.savefig("speedup_64.png", bbox_inches="tight")


    if k == 1024:
        sp1024 = []
        for i in range(len(tparallel[k])):
            sp1024.append(tserial[k]/tparallel[k][i])

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 5, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylabel("time (ms)")
        plt.plot(tparallel[k], label="Time", color="blue", marker='x')
        plt.title("Game of Life in 1024×1024 table")
        plt.savefig("time_1024.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 5, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylabel("speedup")
        plt.plot(sp1024, label="Speedup", color="blue", marker='x')
        plt.title("Game of Life in 1024×1024 table")
        plt.savefig("speedup_1024.png", bbox_inches="tight")

    if k == 4096:
        sp4096 = []
        for i in range(len(tparallel[k])):
            sp4096.append(tserial[k]/tparallel[k][i])

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 5, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylabel("time (ms)")
        plt.plot(tparallel[k], label="Time", color="blue", marker='x')
        plt.title("Game of Life in 4096×4096 table")
        plt.savefig("time_4096.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 5, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8'], rotation=45)
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylabel("speedup")
        plt.plot(sp4096, label="Speedup", color="blue", marker='x')
        plt.title("Game of Life in 4096×4096 table")
        plt.savefig("speedup_4096.png", bbox_inches="tight")