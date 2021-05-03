import numpy as np
import matplotlib as matp
import matplotlib.pyplot as plt
import math
import random
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
import csv
import pprint

fig = plt.figure(figsize=(6.4,6.4),dpi=100)
ax = fig.add_subplot(1,1,1,title = "tracking",facecolor="0")
p1, = ax.plot([], [],'.',color='0.5',alpha=0.5)
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)

class tracking():
    def __init__(self,particle,steps):
        self.n = steps
        self.p = particle
        self.pos_x = np.zeros([self.p])
        self.pos_y = np.zeros([self.p])
        self.tot_x = np.zeros([self.p])
        self.tot_y = np.zeros([self.p])
    def step(self):
        for i in range(self.n):
            theta = 2.0*np.pi*np.random.random(self.p)
            self.pos_x = self.pos_x + np.cos(theta)*np.random.random(self.p)
            self.pos_y = self.pos_y + np.sin(theta)*np.random.random(self.p)
            self.tot_x = np.vstack([self.tot_x,self.pos_x])
            self.tot_y = np.vstack([self.tot_y,self.pos_y])
        tot_x = self.tot_x
        tot_y = self.tot_y
        return tot_x,tot_y


#この量だと重い，5分以上かかる
particle = 12000
steps = 2000

tk = tracking(particle,steps)
tot_x,tot_y = tk.step()

def update(i):
    p1.set_data((tot_x[i,:],tot_y[i,:]))
    return ax
ani = FuncAnimation(fig,update,frames= steps,interval = 10)
ani.save('rw2d_anim_flow4.mp4', writer="ffmpeg",dpi=200)
