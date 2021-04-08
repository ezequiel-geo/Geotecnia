import pandas
import numpy
import tkinter
import mplstereonet
from tkinter import *
import matplotlib.pyplot as plt



strike1, dip1 = 10, 30
strike2, dip2 = 315, 78

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='stereonet')
ax.plane(strike1, dip1, c='b', label='Bedding %03d/%02d' % (strike1, dip1))
ax.plane(strike2, dip2, c='r', label='Fault %03d/%02d' % (strike2, dip2))
ax.legend()
plunge, bearing = mplstereonet.plane_intersection(strike1, dip1, strike2, dip2)
ax.line(plunge, bearing, 'ko', markersize=5, label='Intersection %02d/%03d' % (plunge, bearing))
ax.legend()
# We can also add a grid
ax.grid()
fig

plt.show()

