import imageio
import numpy as np
import os

from skimage import io
import scipy.ndimage as scp


"""
Some transform function to apply to images, input are 2d or 3d arrays, output 2d or 3d arrays
"""

def resize(in_array, **kwargs):
    scale = kwargs.get("scale")
    resized = scp.zoom(in_array, scale, order=3)
    return resized


def convolution(in_array, **kwargs):
    sigmaxy = kwargs.get('sigmaxy')

    twoD = len(in_array.shape) == 2
    if not twoD:
        sigmaz = kwargs.get('sigmaz')
        convolved_image = scp.gaussian_filter(in_array, [sigmaz, sigmaxy, sigmaxy])
    else:
        convolved_image = scp.gaussian_filter(in_array, [sigmaxy, sigmaxy])
    return convolved_image

def crop(in_array, **kwargs):
    x_size = kwargs.get('x_size')
    y_size = kwargs.get('y_size')
    in_array_cropped = None

    if len(in_array.shape) == 3:
        z_size = kwargs.get('z_size')
        midz, midx, midy = len(in_array) // 2, len(in_array[0]) // 2, len(in_array[0][0]) // 2
        minz, minx, miny = midz - z_size // 2, midx - x_size // 2, midy - y_size // 2
        maxz, maxx, maxy = minz + z_size, minx + x_size, miny + y_size
        if minx >= 0 and miny >= 0 and minz >= 0 and maxz < len(in_array) and maxx < len(
                in_array[0]) and maxy < len(in_array[0][0]):
            in_array_cropped = in_array[minz:maxz, minx:maxx, miny:maxy]



    if len(in_array.shape) == 2:
        midx, midy = len(in_array) // 2, len(in_array[0]) // 2
        minx, miny = midx - x_size // 2, midy - y_size // 2
        maxx, maxy = minx + x_size, miny + y_size
        if minx >= 0 and miny >= 0 and maxx <= len(in_array) and maxy <= len(in_array[0]):
            in_array_cropped = in_array[minx:maxx, miny:maxy]

    return in_array_cropped

def cross_section(array3D):
    max_intensity = 0
    imax = 0
    for i in range(len(array3D)):
        intensity = sum(sum(array3D[i]))
        if intensity > max_intensity:
            max_intensity = intensity
            imax = i
    return array3D[imax]

