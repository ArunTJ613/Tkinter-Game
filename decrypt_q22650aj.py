import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("folder",type=str,nargs = "+")
args = parser.parse_args()
folders = args.folder
files = os.listdir(folders[0])
if os.path.isdir(folders[1]):
    pass
else:
    os.mkdir(folders[1])
for file in files:
    f = open(folders[0] + "/" + file,"r")
    data = f.read()
    data = data.strip()
    data = data.strip("\n")
    if data[0] == "H" or data[0] == "h":
        colon = data.index(":")
        length = len(data)
        hexstr = data[colon+1:length]
        decrypt = bytes.fromhex(hexstr)
        decrypt = decrypt.decode("ascii")
    elif data[0] == "C" or data[0] == "c":
        colon = data.index(":")
        length = len(data)
        string = data[colon+1:length]
        caestring =string.lower()
        encryption = "xyzabcdefghijklmnopqrstuvwxyz"
        lengthstr = len(string)
        decrypt = ""
        for a in range(0,lengthstr):
            char = string[a]
            if char == " ":
                decrypt+=" "
                continue
            for b in range(3,len(encryption)):
                if char == encryption[b]:
                    decryptchar = encryption[b-3]
                    decrypt+=decryptchar
                else:
                    pass
    else:
        colon = data.index(":")
        length = len(data)
        morsestr = data[colon+1:length]
        morse = morsestr.split()
        morsecode = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z",".---":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0","._":"a","_...":"b","_._.":"c","_..":"d",".":"e",".._.":"f","__.":"g","....":"h","..":"i",
        ".___":"j","_._":"k","._..":"l","__":"m","_.":"n","___":"o",".__.":"p","__._":"q","._.":"r","...":"s","_":"t",".._":"u","..._":"v",".__":"w","_.._":"x","_.__":"y","__..":"z",".___":"1","..___":"2","...__":"3","...._":"4",".....":"5","_....":"6","__...":"7","___..":"8","____.":"9","_____":"0"}
        lengthstr = len(morsestr)
        keys = morsecode.keys()
        decrypt = ""
        for a in morse:
            if a == "/":
                decrypt+=" "
            else:
                for i in keys:
                    if a == i:
                        decrypt+=morsecode[i]
                    else:
                       pass

    f.close()
    dotindex = file.index(".")
    filename = file[0:dotindex]
    decryptlower = decrypt.lower()
    O = open(folders[1] + "/" + filename + "_q22650aj.txt","w")
    O.write(decryptlower)
    O.close()
