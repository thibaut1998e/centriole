import os
import sys

_, folder, deleteList = sys.argv


#folder = '/Users/Denis/Documents/data/superres_centriole/Assembly_tif_clean'
#deleteList ='/Users/Denis/Documents/data/superres_centriole/deleteList.txt'

deleteListFile = open(deleteList, 'r', errors='ignore')
Lines = deleteListFile.readlines()
for line in Lines:
    print(line)
    tmp = folder+'/deconv/c1/'+line[:-1]+'.tiff'
    if os.path.exists(tmp):
        os.remove(tmp)
    tmp = folder+'/deconv/c2/'+line[:-1]+'.tiff'
    if os.path.exists(tmp):
        os.remove(tmp)
    tmp = folder+'/raw/c1/'+line[:-1]+'.tiff'
    if os.path.exists(tmp):
        os.remove(tmp)
    tmp = folder+'/raw/c2/'+line[:-1]+'.tiff'
    if os.path.exists(tmp):
        os.remove(tmp)
