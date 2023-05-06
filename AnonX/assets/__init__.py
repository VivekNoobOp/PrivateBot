from os import listdir

bgs = []
for file in listdir("AnonX/assets"):
    if file.endswith("png"):
        bgs.append(file[:-4])
