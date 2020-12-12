import matplotlib.pyplot as plt
import numpy as np

## Jacobi Method
j2048 = {}
j2048['serial'] = 7.507741
j2048['parallel'] = [8.418097,4.321809,2.434777,1.463781,1.090206,0.695447,0.539651]

j4096 = {}
j4096['serial'] = 30.222466
j4096['parallel'] = [33.636416,16.990405,9.275748,5.348449,4.270647,4.006805,3.689206]

j6144 = {}
j6144['serial'] = 67.385763
j6144['parallel'] = [75.623320,38.080276,20.606649,11.752673,9.384581,9.039419,8.663320]

## Gauss Method
g2048 = {}
g2048['serial'] = 7.507741
g2048['parallel'] = [8.418097,4.321809,2.434777,1.463781,1.090206,0.695447,0.539651]

g4096 = {}
g4096['serial'] = 30.222466
g4096['parallel'] = [33.636416,16.990405,9.275748,5.348449,4.270647,4.006805,3.689206]

g6144 = {}
g6144['serial'] = 67.385763
g6144['parallel'] = [75.623320,38.080276,20.606649,11.752673,9.384581,9.039419,8.663320]

## Red-Black Method
r2048 = {}
r2048['serial'] = 7.507741
r2048['parallel'] = [8.418097,4.321809,2.434777,1.463781,1.090206,0.695447,0.539651]

r4096 = {}
r4096['serial'] = 30.222466
r4096['parallel'] = [33.636416,16.990405,9.275748,5.348449,4.270647,4.006805,3.689206]

r6144 = {}
r6144['serial'] = 67.385763
r6144['parallel'] = [75.623320,38.080276,20.606649,11.752673,9.384581,9.039419,8.663320]


for k in 2048,4096,6144:

    if k == 2048:
        jspeedup2048 = []
        for i in range(7):
            jspeedup2048.append(j2048['serial']/j2048['parallel'][i])

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 7, 1))
        ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 6.5)
        ax.set_ylabel("time (s)")
        plt.plot(j2048['parallel'], label="B=jacobi", color="yellow", marker='x')
        plt.title("Jacobi Edition in 2048×2048 table")
        plt.legend()
        plt.savefig("time_jacobi2048.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 7, 1))
        ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 6.5)
        ax.set_ylabel("speedup")
        plt.plot(jspeedup2048, label="B=jacobi", color="yellow", marker='x')
        plt.title("Jacobi Method Speedup in 2048×2048 table")
        plt.legend()
        plt.savefig("speedup_jacobi2048.png", bbox_inches="tight")

        labels = ['Jacobi', 'Gauss', 'Red-Black']
        a1 = [j2048['parallel'][3], 34, 30, 35, 27]
        a2 = [j2048['parallel'][4], 32, 34, 20, 25]
        a3 = [j2048['parallel'][5], 34, 30, 35, 27]
        a4 = [j2048['parallel'][6], 34, 30, 35, 27]
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, a1[0], width, label="8")
        rects2 = ax.bar(x - width/2, a2[0], width, label="16")
        rects3 = ax.bar(x + width/2, a3[0], width, label="32")
        rects4 = ax.bar(x + width, a4[0], width, label="64")
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Total Time (s)')
        ax.set_title('Total Time')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        #def autolabel(rects):
        ##"""Attach a text label above each bar in *rects*, displaying its height."""
        #    for rect in rects:
        #        height = rect.get_height()
        #        ax.annotate('{}'.format(height),
        #                    xy=(rect.get_x() + rect.get_width() / 2, height),
        #                    xytext=(0, 3),  # 3 points vertical offset
        #                    textcoords="offset points",
        #                    ha='center', va='bottom')
        #autolabel(rects1)
        #autolabel(rects2)
        #autolabel(rects3)
        #autolabel(rects4)
        #fig.tight_layout()
        plt.savefig("Total Time 2048.png", bbox_inches="tight")


    if k == 4096:
        jspeedup4096 = []
        for i in range(7):
            jspeedup4096.append(j4096['serial']/j4096['parallel'][i])
            
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 7, 1))
        ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 6.5)
        ax.set_ylabel("time (s)")
        plt.plot(j4096['parallel'], label="B=jacobi", color="yellow", marker='x')
        plt.title("Jacobi Edition in 4096×4096 table")
        plt.legend()
        plt.savefig("time_jacobi4096.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 7, 1))
        ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 6.5)
        ax.set_ylabel("speedup")
        plt.plot(jspeedup4096, label="B=jacobi", color="yellow", marker='x')
        plt.title("Jacobi Method Speedup in 4096×4096 table")
        plt.legend()
        plt.savefig("speedup_jacobi4096.png", bbox_inches="tight")
    
        labels = ['Jacobi', 'Gauss', 'Red-Black']
        a1 = [j4096['parallel'][3], 34, 30, 35, 27]
        a2 = [j4096['parallel'][4], 32, 34, 20, 25]
        a3 = [j4096['parallel'][5], 34, 30, 35, 27]
        a4 = [j4096['parallel'][6], 34, 30, 35, 27]
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, a1[0], width, label="8")
        rects2 = ax.bar(x - width/2, a2[0], width, label="16")
        rects3 = ax.bar(x + width/2, a3[0], width, label="32")
        rects4 = ax.bar(x + width, a4[0], width, label="64")
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Total Time (s)')
        ax.set_title('Total Time')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        #def autolabel(rects):
        ##"""Attach a text label above each bar in *rects*, displaying its height."""
        #    for rect in rects:
        #        height = rect.get_height()
        #        ax.annotate('{}'.format(height),
        #                    xy=(rect.get_x() + rect.get_width() / 2, height),
        #                    xytext=(0, 3),  # 3 points vertical offset
        #                    textcoords="offset points",
        #                    ha='center', va='bottom')
        #autolabel(rects1)
        #autolabel(rects2)
        #autolabel(rects3)
        #autolabel(rects4)
        fig.tight_layout()
        plt.savefig("Total Time 4096.png", bbox_inches="tight")

    if k == 6144:
        jspeedup6144 = []
        for i in range(7):
            jspeedup6144.append(j6144['serial']/j6144['parallel'][i])   

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 7, 1))
        ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 6.5)
        ax.set_ylabel("time (s)")
        plt.plot(j6144['parallel'], label="B=jacobi", color="yellow", marker='x')
        plt.title("Jacobi Edition in 6144×6144 table")
        plt.legend()
        plt.savefig("time_jacobi6144.png", bbox_inches="tight")

        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlabel("number of cores")
        ax.xaxis.set_ticks(np.arange(0, 7, 1))
        ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
        ax.set_xlim(-0.5, 6.5)
        ax.set_ylabel("speedup")
        plt.plot(jspeedup6144, label="B=jacobi", color="yellow", marker='x')
        plt.title("Jacobi Method Speedup in 6144×6144 table")
        plt.legend()
        plt.savefig("speedup_jacobi6144.png", bbox_inches="tight")
        
        labels = ['Jacobi', 'Gauss', 'Red-Black']
        a1 = [j6144['parallel'][3], 34, 30, 35, 27]
        a2 = [j6144['parallel'][4], 32, 34, 20, 25]
        a3 = [j6144['parallel'][5], 34, 30, 35, 27]
        a4 = [j6144['parallel'][6], 34, 30, 35, 27]
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, a1[0], width, label="8")
        rects2 = ax.bar(x - width/2, a2[0], width, label="16")
        rects3 = ax.bar(x + width/2, a3[0], width, label="32")
        rects4 = ax.bar(x + width, a4[0], width, label="64")
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Total Time (s)')
        ax.set_title('Total Time')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        #def autolabel(rects):
        #"""Attach a text label above each bar in *rects*, displaying its height."""
        #    for rect in rects:
        #        height = rect.get_height()
        #        ax.annotate('{}'.format(height),
        #                    xy=(rect.get_x() + rect.get_width() / 2, height),
        #                    xytext=(0, 3),  # 3 points vertical offset
        #                    textcoords="offset points",
        #                    ha='center', va='bottom')
        #autolabel(rects1)
        #autolabel(rects2)
        #autolabel(rects3)
        #autolabel(rects4)
        fig.tight_layout()
        plt.savefig("Total Time 6144.png", bbox_inches="tight")