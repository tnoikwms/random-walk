from os import W_OK
import numpy as np
import matplotlib as matp
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
import csv
import pprint

#ここクラス
class randomwalk:
    def __init__(self,N,particle):
        self.fig = plt.figure(figsize=(6.4,6.4),dpi=100)
        #self.a = self.fig.add_subplot(1,1,1,title = "tracking")
        self.col = self.fig.add_subplot(1,1,1,title = "distribution")
        self.n = N
        self.p = particle
        self.totalsave = np.zeros((self.n+1,2),dtype=int)
        self.last = np.zeros([2],dtype = int)
    #複数粒子の分布を調べたい
    def total(self):
        for j in range(0,self.p):
            self.x = np.zeros([2],dtype = int)
            self.tot = self.x
            for i in range(0,self.n):
                r = random.randint(-1,1)
                direction = random.randint(0,1)
                if direction == 0:
                    self.x[0] += r
                else:
                    self.x[1] += r
                if i == self.n-1:
                    self.last = np.vstack(([self.last,self.x]))
                self.tot = np.vstack(([self.tot, self.x]))
            self.totalsave = np.hstack((self.totalsave,self.tot))

    #追跡のアニメーションを作る
    def anima(self):

    #csvに出力
    def output(self):
        np.savetxt('particle_tracking.csv',self.totalsave,fmt='%d')
    #分布をヒストグラムとして表示する
    def hist(self):
        self.h = self.col.hist2d(self.last[:,0],self.last[:,1],(320,320),cmap=cm.jet)
        self.h[3].set_clim(0,3)
        self.fig.colorbar(self.h[3])
    #表示
    def show(self):
        print(self.last)

step = 100
particle = 10

rk = randomwalk(step,particle)

#複数の粒子の分布
rk.total()


#rk.output()
#rk.hist()
#plt.show()
#rk.anima()