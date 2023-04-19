""" LIBRARIES USED """
import numpy as np
import csv
import random
#import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
                                            ##---CODE----
r1=int(input('Enter starting point'))
r2=int(input('Enter ending point'))
nv=float(input("Enter the number of values"))
val=abs(r1)+abs(r2)
stepsize=val/nv;
vals={}#Empty dictionary for values
                                        ##-----CSV FILE-----
path=open("Readings(x,y).csv","w")#open csv file

for i in np.arange(r1,r2+stepsize,stepsize):
    output = random.random()
    vals[i]=output
#print(vals)

z=csv.writer(path)
for x,y in vals.items():#write data into csv file
    z.writerow([x,y])

path.close()
df = pd.read_csv('Readings(x,y).csv', header=None)
df.rename(columns={0: 'X', 1: 'Y'}, inplace=True)#header names
df.to_csv('Readings(x,y).csv', index=False)
                                    #----PLOTTING----
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["X", "Y"]
df = pd.read_csv("Readings(x,y).csv", usecols=columns)
print("Contents in csv file:\n", df)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Random Generated Graph")
plt.plot(df.X, df.Y)
plt.savefig('RGG.png')
plt.show()

#df = pd.read_csv('Readings(x,y).csv')
#print(df)




