import argparse
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

parser=argparse.ArgumentParser()
parser.add_argument("-grid","--grid",help="grid file to graph")
parser.add_argument("-title","--title",help="title of plot")
args=parser.parse_args()

def convert_CV2(value):
    return(int(value*100))

def convert_CV1(value):
    return(int(value*100))

data=[]
f = open(args.grid)
for i in f.readlines()[9:]:
    if len(i.strip()) ==0:
        pass
    else:data.append(i)

previous_angle = float(data[0].split()[1])
local,arr=[],[]
for row in data:
    angle = float(row.split()[1])
    if angle == previous_angle:
        local.append(float(row.split()[2]))
    else:
        arr.append(local)
        previous_angle=angle
        local=[]
        local.append(float(row.split()[2]))

arr =np.array(arr)* .239


ytick = np.around(np.linspace(0,10,1000),3)
xtick = np.around(np.linspace(0,10,1000),3)
cmap = sns.light_palette("navy")
graph = sns.heatmap(arr,vmin=np.amin(arr),vmax=np.amax(arr),
    yticklabels=ytick,xticklabels=xtick,cmap=cmap)

for ind,label in enumerate(graph.get_yticklabels()):
    if ind%50 == 0:
        label.set_visible(True)
    else: label.set_visible(False)

for ind,label in enumerate(graph.get_xticklabels()):
    if ind%50 == 0:
        label.set_visible(True)
    else: label.set_visible(False)

graph.set_xlim(0,500)
graph.set_ylim(0,500)
graph.set(ylabel='phi [rad]',xlabel='d [mE-11]')
plt.show()
