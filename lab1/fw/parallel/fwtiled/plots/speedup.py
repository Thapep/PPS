import matplotlib.pyplot as plt
import re
import numpy as np
serial = open('../../../serial/fw_tiled.out','r')
lines = serial.readlines()

ts1024 = {}
ts1024[32] = []
ts1024[64] = []
ts1024[128] = []
ts1024[256] = []
ts2048 = {}
ts2048[32] = []
ts2048[64] = []
ts2048[128] = []
ts2048[256] = []
ts4096 = {}
ts4096[32] = []
ts4096[64] = []
ts4096[128] = []
ts4096[256] = []
l = []
for i in range(len(lines)):
    l.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    if int(l[i][0])==1024:
        ts1024[int(l[i][1])].append((float(l[i][2])))
    if int(l[i][0])==2048:
        ts2048[int(l[i][1])].append((float(l[i][2])))
    if int(l[i][0])==4096:
        ts4096[int(l[i][1])].append((float(l[i][2])))  
print(ts1024)
print(ts2048)
print(ts4096)


parallel = open('./fw_tiled.out','r')
lines = parallel.readlines()

tp1024 = {}
tp1024[32] = []
tp1024[64] = []
tp1024[128] = []
tp1024[256] = []
tp2048 = {}
tp2048[32] = []
tp2048[64] = []
tp2048[128] = []
tp2048[256] = []
tp4096 = {}
tp4096[32] = []
tp4096[64] = []
tp4096[128] = []
tp4096[256] = []
p = []
for i in range(len(lines)):
    p.append(re.findall(r'[+-]?\d+(?:\.\d+)?', lines[i]))
    if len(p[i])==1:
        continue
    if int(p[i][0])==1024:
        tp1024[int(p[i][1])].append((float(p[i][2])))
    if int(p[i][0])==2048:
        tp2048[int(p[i][1])].append((float(p[i][2])))
    if int(p[i][0])==4096:
        tp4096[int(p[i][1])].append((float(p[i][2])))    
print(tp1024)
print(tp2048)
print(tp4096)

for k in 1024,2048,4096:

    if k == 1024:
        sp1024_32 = []
        for i in range(len(tp1024[32])):
            sp1024_32.append(ts1024[32][0]/tp1024[32][i])

        sp1024_64 = []
        for i in range(len(tp1024[64])):
            sp1024_64.append(ts1024[64][0]/tp1024[64][i])
        
        sp1024_128 = []
        for i in range(len(tp1024[128])):
            sp1024_128.append(ts1024[128][0]/tp1024[128][i])

        sp1024_256 = []
        for i in range(len(tp1024[256])):
            sp1024_256.append(ts1024[256][0]/tp1024[256][i])    
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("time (s)")
        plt.plot(tp1024[32], label="B=32", color="yellow", marker='x')
        plt.plot(tp1024[64], label="B=64", color="blue", marker='x')
        plt.plot(tp1024[128], label="B=128", color="red", marker='x')
        plt.plot(tp1024[256], label="B=256", color="green", marker='x')
        plt.title("Floyd-Warshall Recursive Edition in 1024×1024 table")
        plt.legend()
        plt.savefig("time_fw1024.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("speedup")
        plt.plot(sp1024_32, label="B=32", color="yellow", marker='x')
        plt.plot(sp1024_64, label="B=64", color="blue", marker='x')
        plt.plot(sp1024_128, label="B=128", color="red", marker='x')
        plt.plot(sp1024_256, label="B=256", color="green", marker='x')
        plt.title("Floyd-Warshall Recursive Edition in 1024×1024 table")
        plt.legend()
        plt.savefig("speedup_fw1024.png", bbox_inches="tight")


    if k == 2048:
        sp2048_32 = []
        for i in range(len(tp2048[32])):
            sp2048_32.append(ts2048[32][0]/tp2048[32][i])

        sp2048_64 = []
        for i in range(len(tp2048[64])):
            sp2048_64.append(ts2048[64][0]/tp2048[64][i])
        
        sp2048_128 = []
        for i in range(len(tp2048[128])):
            sp2048_128.append(ts2048[128][0]/tp2048[128][i])

        sp2048_256 = []
        for i in range(len(tp2048[256])):
            sp2048_256.append(ts2048[256][0]/tp2048[256][i])    

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("time (s)")
        plt.plot(tp2048[32], label="B=32", color="yellow", marker='x')
        plt.plot(tp2048[64], label="B=64", color="blue", marker='x')
        plt.plot(tp2048[128], label="B=128", color="red", marker='x')
        plt.plot(tp2048[256], label="B=256", color="green", marker='x')
        plt.title("Floyd-Warshall Recursive Edition in 2048×2048 table")
        plt.legend()
        plt.savefig("time_fw2048.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("speedup")
        plt.plot(sp2048_32, label="B=32", color="yellow", marker='x')
        plt.plot(sp2048_64, label="B=64", color="blue", marker='x')
        plt.plot(sp2048_128, label="B=128", color="red", marker='x')
        plt.plot(sp2048_256, label="B=256", color="green", marker='x')
        plt.title("Floyd-Warshall Recursive Edition in 2048×2048 table")
        plt.legend()
        plt.savefig("speedup_fw2048.png", bbox_inches="tight")

    if k == 4096:
        sp4096_32 = []
        for i in range(len(tp4096[32])):
            sp4096_32.append(ts4096[32][0]/tp4096[32][i])

        sp4096_64 = []
        for i in range(len(tp4096[64])):
            sp4096_64.append(ts4096[64][0]/tp4096[64][i])
        
        sp4096_128 = []
        for i in range(len(tp4096[128])):
            sp4096_128.append(ts4096[128][0]/tp4096[128][i])

        sp4096_256 = []
        for i in range(len(tp4096[256])):
            sp4096_256.append(ts4096[256][0]/tp4096[256][i]) 

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("time (s)")
        plt.plot(tp4096[32], label="B=32", color="yellow", marker='x')
        plt.plot(tp4096[64], label="B=64", color="blue", marker='x')
        plt.plot(tp4096[128], label="B=128", color="red", marker='x')
        plt.plot(tp4096[256], label="B=256", color="green", marker='x')
        plt.title("Floyd-Warshall Recursive Edition in 4096×4096 table")
        plt.legend()
        plt.savefig("time_fw4096.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 8, 1))
        ax.set_xticklabels(['1', '2', '4', '6', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylabel("speedup")
        plt.plot(sp4096_32, label="B=32", color="yellow", marker='x')
        plt.plot(sp4096_64, label="B=64", color="blue", marker='x')
        plt.plot(sp4096_128, label="B=128", color="red", marker='x')
        plt.plot(sp4096_256, label="B=256", color="green", marker='x')
        plt.title("Floyd-Warshall Recursive Edition in 4096×4096 table")
        plt.legend()
        plt.savefig("speedup_fw4096.png", bbox_inches="tight")