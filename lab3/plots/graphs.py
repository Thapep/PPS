import matplotlib.pyplot as plt
import numpy as np

exec1 = [324.56, 646.29, 1239.20, 2149.40, 1807.82, 3511.06, 6496.43]
exec2 = [302.74, 648.97, 1269.27, 2201.59, 1998.92, 8258.84, 6571.36]

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel("number of cores")
ax.xaxis.set_ticks(np.arange(0, 7, 1))
ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
ax.set_xlim(-0.5, 6.5)
ax.set_ylabel("Throughput (Mops/sec)")
plt.plot(exec1, label="execution 1", color="blue", marker='x')
plt.plot(exec2, label="execution 2", color="red", marker='x')
plt.title("Throughput")
plt.legend()
plt.savefig("throughput_bank_opt.png", bbox_inches="tight")

