import os
from skimage import io
import numpy as np
import imageio
import shutil
import transforms as tf

def transform(folder_in, folder_out, funcs_to_apply, **kwargs):
    #apply all the funcion in the list functs_to_apply (in the same order)
    # to all the images in folder_in and store them in folder_out
    nb_files_written = 0
    types = ["deconv", "raw"]
    channels = ["c1", "c2"]
    if os.path.exists(folder_out):
        shutil.rmtree(folder_out)
    for typ in types:
        os.makedirs(folder_out + "/" + typ)
        for channel in channels:
            os.makedirs(folder_out + "/" + typ + "/" + channel)
            folder_path = folder_in + "/" + typ + "/" + channel
            #n first images of the folder
            file_names = os.listdir(folder_path)#[:n]
            for name in file_names:
                image_path = folder_path + "/" + name
                image = io.imread(image_path)
                im_array = np.array(image)
                for f in funcs_to_apply:
                    im_array = f(im_array, **kwargs)

                if isinstance(im_array, np.ndarray):
                    pathToWrite = folder_out + "/" + typ + "/" + channel + "/" + name
                    if len(im_array.shape) == 2:
                        imageio.imwrite(pathToWrite, im_array)
                        nb_files_written += 1
                    elif len(im_array.shape) == 3:
                        imageio.mimwrite(pathToWrite, im_array)
                        nb_files_written += 1
                    else:
                        print("can't write image")
                else:
                    print("image is not a numpy array")

    print(f'{nb_files_written} files were written')



#folderIn = "C:/Users/Thibaut/Documents/_Stage_Image_Super_Resolution/data/denis_thunder_tiff"
#folderOut = "C:/Users/Thibaut/Documents/_Stage_Image_Super_Resolution/data/denis_thunder_crosscrop"

folderIn = "/home/eloy/cropped2D"
folderOut = "/home/eloy/cropped_convolved2D"


transform(folderIn, folderOut, [tf.convolution, tf.resize], scale=0.5, sigmaxy=5)


