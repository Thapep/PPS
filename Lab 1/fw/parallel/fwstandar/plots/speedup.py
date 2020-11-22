import matplotlib.pyplot as plt
import re
import numpy as np
serial = open('../serial/fw.out','r')
lines = serial.readlines()

tserial = {}
l = []
for i in range(len(lines)):
    l.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    tserial[int(l[i][0])] = (float(l[i][1])) 

parallel = open('fwstandar/fw.out','r')
lines = parallel.readlines()

tparallel = {}
tparallel[1024] = []
tparallel[2048] = []
tparallel[4096] = []
p = []
for i in range(len(lines)):
    p.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    if len(p[i])==1:
        continue
    tparallel[int(p[i][0])].append((float(p[i][1])))
print(tparallel)
for k in tparallel.keys():

    if k == 1024:
        sp1024 = []
        for i in range(len(tparallel[k])):
            sp1024.append(tserial[k]/tparallel[k][i])
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("time (ms)")
        plt.plot(tparallel[k], label="Time", color="blue", marker='x')
        plt.title("Floyd-Warshall Standar Edition in 1024×1024 table")
        plt.savefig("time_fw1024.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("speedup")
        plt.plot(sp1024, label="Speedup", color="blue", marker='x')
        plt.title("Floyd-Warshall Standar Edition in 1024×1024 table")
        plt.savefig("speedup_fw1024.png", bbox_inches="tight")


    if k == 2048:
        sp2048 = []
        for i in range(len(tparallel[k])):
            sp2048.append(tserial[k]/tparallel[k][i])

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("time (ms)")
        plt.plot(tparallel[k], label="Time", color="blue", marker='x')
        plt.title("Floyd-Warshall Standar Edition in 2048×2048 table")
        plt.savefig("time_fw2048.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("speedup")
        plt.plot(sp2048, label="Speedup", color="blue", marker='x')
        plt.title("Floyd-Warshall Standar Edition in 2048×2048 table")
        plt.savefig("speedup_fw2048.png", bbox_inches="tight")

    if k == 4096:
        sp4096 = []
        for i in range(len(tparallel[k])):
            sp4096.append(tserial[k]/tparallel[k][i])

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("time (ms)")
        plt.plot(tparallel[k], label="Time", color="blue", marker='x')
        plt.title("Floyd-Warshall Standar Edition in 4096×4096 table")
        plt.savefig("time_fw4096.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("speedup")
        plt.plot(sp4096, label="Speedup", color="blue", marker='x')
        plt.title("Floyd-Warshall Standar Edition in 4096×4096 table")
        plt.savefig("speedup_fw4096.png", bbox_inches="tight")