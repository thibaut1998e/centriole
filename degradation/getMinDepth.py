import os
from skimage import io
import numpy as np
import sys

path = "C:/Users/Thibaut/Documents/_Stage_Image_Super_Resolution/data/assembly_tiff"

listX = []
listY = []
listZ = []
i = 0

for type in ["deconv", "raw"]:

    print(type)
    for channel in ["c1", "c2"]:
        folder_path = path + "/" + type + "/" + channel
        print(channel)
        for name in os.listdir(folder_path):
            print(i)
            image_path = folder_path + "/" + name
            x,y,z = io.imread(image_path).shape
            listX.append(x)
            listY.append(y)
            listZ.append(z)
            i += 1

print("minx",min(listX))
print("miny", min(listY))
print("minz", min(listZ))

print("meanx", np.mean(listX))
print("meany", np.mean(listY))
print("meanz", np.mean(listZ))

print("stdx", np.std(listX))
print("stdy", np.std(listY))
print("stdz", np.std(listZ))

listX.sort()
listY.sort()
listZ.sort()
print(listX)
print(listY)
print(listZ)


