import os
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

resultpath=r'C:\Users\eivinhug\NTNU\PhD\AbaqusModels\SplitDisk\Split_Friciton_study_Wo_Hole'
writefile=r'C:\Users\eivinhug\NTNU\PhD\AbaqusModels\SplitDisk\Split_Friciton_study_Wo_Hole_Results'
if not os.path.exists(writefile):
    os.makedirs(writefile)

files= [f for f in listdir(resultpath) if isfile(join(resultpath, f))]
rptfiles=[]
for f in files:
    if f.split(".")[-1]=="rpt":
        rptfiles.append(f)

print(rptfiles)

for f in rptfiles:
    filepath=resultpath+"\\"+f
    file=open(filepath,"r")
    filelines=file.readlines()

    #filename=filelines[1].strip()+((filelines[1].strip()+filelines[2].strip()).split("X"))[1].strip()+".txt" #mesh study
    
    filename=filelines[1].strip()+(f.split(".")[0]+".txt") #friction study
    
    resultfilenamepath=writefile+"\\"+filename
    resultfile = open(resultfilenamepath, "w+")
    
    n=0
    for entry in filelines:
        cleanentry=entry.strip()

        n=n+1
        if n>4 and cleanentry!="":
            resultfile.write((cleanentry.split(" ")[0]).strip()+'\t'+(cleanentry.split(" ")[-1]).strip()+'\n')
    resultfile.close()
    
files= [f for f in listdir(writefile) if isfile(join(writefile, f))]
rptfiles=[]
for f in files:
    if f.split(".")[-1]=="txt" and f.split("_")[0]=="LE11":
        rptfiles.append(f)

fig = plt.figure()
ax = plt.axes()

for f in rptfiles:
    openfile=writefile+"\\"+f
    file=open(openfile,"r")
    filelines=file.readlines()
    x=[]
    y=[]
    print(file)
    for entry in filelines:
        X=entry.split("\t")[0]
        Y=entry.split("\t")[1]
        x.append(float(X))
        y.append(float(Y))
            
    ax.plot(x,y)
    files= [f for f in listdir(writefile) if isfile(join(writefile, f))]
rptfiles=[]


for f in files:
    if f.split(".")[-1]=="txt" and f.split("_")[0]=="LE22":
        rptfiles.append(f)


fig2 = plt.figure()
ax2 = plt.axes()

for f in rptfiles:
    openfile=writefile+"\\"+f
    file=open(openfile,"r")
    filelines=file.readlines()
    x=[]
    y=[]
    for entry in filelines:
        X=entry.split("\t")[0]
        Y=entry.split("\t")[1]
        x.append(float(X))
        y.append(float(Y))
            
    ax2.plot(x,y)    

plt.show()


    

        




