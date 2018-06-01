#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 5
xlabel = 'Grupos'
ylabel = 'Valor'
title = 'Prueba'

means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

ind = range(n_groups)
b_width = 0.25

opacity = 0.4
error_config = {'ecolor': '0.3'}

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ticks = [x + b_width / 2 for x in ind]
ax.set_xticks(ticks)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()
ax.bar(ticks,[2,3,2,2,5],label='Algo')
plt.savefig('Prueba.png')# Credit: Josh Hemann
