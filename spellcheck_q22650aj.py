import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("folder",type=str,nargs = "+")
args = parser.parse_args()
folders = args.folder
files = os.listdir(folders[1])
if os.path.isdir(folders[2]):
    pass
else:
    os.mkdir(folders[2])
f = open(folders[0],"r")
data = f.read()
Dictionary = data.split()
f.close()
for file in files:
    f = open(folders[1] + "/" + file,"r")
    data = f.read()
    newdata = data.strip()
    newerdata = newdata.strip("\n")
    correcteddata = ""
    numcount = 0
    specialcount = 0
    upcase=0
    for a in range(0,len(newerdata)):
        if newerdata[a].isalpha():
            if newerdata[a].isupper():
                b = newerdata[a].lower()
                correcteddata+=b
                upcase+=1
            else:
                correcteddata+=newerdata[a]
        elif newerdata[a] == " ":
            correcteddata+=newerdata[a]
        elif newerdata[a].isnumeric():
            numcount+=1
        elif newerdata[a] == ".":
            if newerdata[a:a+3] == "...":
                specialcount-=1
            else:
                specialcount+=1
        else:
            specialcount+=1
    words = correcteddata.split()
    wordcount = len(words)
    correctwords = 0
    incorrectwords = 0
    for i in words:
        if i in Dictionary:
            correctwords+=1
        else:
            incorrectwords+=1
    f.close()
    dotindex = file.index(".")
    filename = file[0:dotindex]
    O = open(folders[2] + "/" + filename + "_q22650aj.txt","w")
    O.write("q22650aj\n")
    O.write("Formatting ###################\n")
    O.write("Number of upper case letters changed:" + str(upcase) + "\n")
    O.write("Number of punctuations removed:" + str(specialcount) + "\n")
    O.write("Number of numbers removed:" + str(numcount) + "\n")
    O.write("Spellchecking ###################\n")
    O.write("Number of words:" + str(wordcount) + "\n")
    O.write("Number of correct words:" + str(correctwords) + "\n")
    O.write("Number of incorrect words:" + str(incorrectwords) + "\n")
    O.close()

    #print("Formatting ################### ","Number of upper case words transformed:" + str(upcase),"Number of punctuation’s removed:" + str(specialcount),"Number of numbers removed:" + str(numcount),"Spellchecking ###################","Number of words in file:" + str(wordcount),"Number of correct words in file:" + str(correctwords),"Number of incorrect words in file:" + str(incorrectwords),sep = "\n")
