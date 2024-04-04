import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp

data = hp.get_data('capture01_250Hz.txt')
Fs = 250
time = np.arange(len(data))/Fs

np.random.seed(8608)
t0 = np.random.randint(30, 100)
print(f'Segment starts from: {t0} s')
i = (t0 < time) & (time < t0 + 60)
data2 = data[i]

wd, m = hp.process(data2, sample_rate = Fs)

hp.plotter(wd, m)
plt.show()

for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
