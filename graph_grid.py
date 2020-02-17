import argparse
import matplotlib.pyplot as plt
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument("-grid","--grid",help="list of grids")
parser.add_argument("-title", "--title",help="title")
parser.add_argument("-name","--name",help="outfilename") 
parser.add_argument("-rmsd0","--rmsd0",help="intial rmsd",type=float) 
parser.add_argument("-rstd","--rstd",help="initial rmsd std",type=float)
args=parser.parse_args()

metad=[]
der=[]
f=open(args.grid,'r')
res_list = [i for i in f.readlines()[5:]]
for row in res_list:
    s=row.split()[0]
    metad.append(float(row.split()[1]))
    der.append(float(row.split()[2]))
x = np.arange(0,10.02,.01)

fig, (figure)= plt.subplots(nrows=1, figsize=(8,5))

if args.rmsd0 is not None and args.rstd is not None: 
    index=np.where(x==np.round(args.rmsd0,2))[0][0] 
    print(index,metad[index])
    constant = metad[index]
    metad=np.array(metad)-constant

figure.plot(x,-metad,color='black')

plt.errorbar(x[index],metad[index],xerr=args.rstd,marker='.')
plt.xlim(0,3)
plt.xticks(np.arange(0,3.5,step=0.5))
plt.title(args.title)
plt.xlabel("RMSD")
plt.ylabel("kcal/mol")
plt.savefig(args.name+".png")
