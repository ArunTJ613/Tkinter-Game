import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("folder",type=str,nargs = "+")
args = parser.parse_args()
folders = args.folder
files = os.listdir(folders[0]))
if os.path.isdir(folders[1]):
    pass
else:
    os.mkdir(folders[1])
count=1
for file in files:
    f = open(folders[0] + "/" + file,"r")
    scor=f.read()
    scor = scor.strip()
    scor = scor.strip("\n")
    score=[]
    length=len(scor)
    for a in range(0,length,3):
        a = scor[a:a+3]
        score.append(a)
    Team1=0
    Team2=0
    for i in score:
        if i[1] == "1":
            if i[2] == "t":
                Team1+=5
            elif i[2] == "c":
                Team1+=2
            elif i[2] == "p":
                Team1+=3
            else:
                Team1+=3
        else:
            if i[2] == "t":
                Team2+=5
            elif i[2] == "c":
                Team2+=2
            elif i[2] == "p":
                Team2+=3
            else:
                Team2+=3

    result=str(Team1)+":"+str(Team2)
    dotindex = file.index(".")
    filename = file[0:dotindex]
    f.close()
    O = open(folders[1] + "/" + filename + "_q22650aj.txt","w")
    O.write(result)
    O.close()
    count+=1

#f.close()

#O = open(files[1],"w")
#O.write(result)
#O.close()
