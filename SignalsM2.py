# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft


t = np.linspace(0, 3, 12 * 1024)

c3 = 130.81
d3 = 146.83
e3 = 164.81
f3 = 174.61
g3 = 196
g3b = 207.65
a3 = 220
b3 = 246.93

c4 = 261.63
d4 = 293.66
d4b = 311.12
e4 = 329.63
f4 = 349.23
g4 = 392
g4b = 415.3
a4 = 440
b4 = 493.88

# song: fur elise
# zeros are to pause

right_hand = [e4, d4b, e4, d4b, e4, b3, d4, c4, a3, 0, c3, e3, a3, b3, 0, e3, 
              g3b, b3, c4, 0, e3]
left_hand = 0



starting_time = [i/7 for i in range(len(right_hand))]
how_long = [0.14] * len(right_hand)


def u(t):
    return 1 * (t >= 0)


x = 0
for note in range(len(right_hand)):
    x += (np.sin(2 * np.pi * right_hand[note] * t)) * (
        u(t - starting_time[note]) - u(t - starting_time[note] - how_long[note]))
    
N = 3*1024
F = np.linspace(0, 512, int(N/2))
t = np.linspace(0, 3, 12*1024)  

xf = fft(x)
xf = (2/N)*np.abs(xf [0:np.int(N/2)])
maxp = 0
for i in range(0, len(xf)):
    if(xf[i]>maxp):
        maxp = xf[i]


fn1 = np.random.randint(0, 512, 2)
noise = x + (np.sin(2*np.pi*fn1[0]*t) + np.sin(2*np.pi*fn1[1]*t))
noisef = fft(noise)
noisef = (2/N)*np.abs(noisef [0:np.int(N/2)])
fp = 0
sp = 0
for i in range(0, len(noisef)):
    if(np.int(noisef[i])>maxp and fp == 0 and sp == 0):
        fp = F[i]
    if(np.int(noisef[i])>maxp and fp > 0):
        sp = F[i]
        
xfilter = noise - (np.sin(2*np.pi*np.int(fp)*t) + np.sin(2*np.pi*np.int(sp)*t))


sd.play(x, 3*1024)
plt.plot(t, xfilter)
