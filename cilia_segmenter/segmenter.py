import apoc
import matplotlib.pyplot as plt
import numpy as np
from skimage import morphology
from skimage.color import label2rgb

def cilia_binarization (img):
    """
    This function binarises the cilia channel from an image array by predicting foreground and background and returns an array.
    Note: the only possible input is the cilia channel where the dimensions are the z stack and the size of the image. [:,:,:].
    Parameters:
    img: bool ndarray
        Variable containing the loaded image (cilia channel).
    """
    segmenter = apoc.PixelClassifier(opencl_filename='D:/estela/src/PixelClassifier.cl')
    binarized_img = segmenter.predict(image=img)
    binarized_array = np.array(binarized_img) >1 # The array is converted to boolean to have 0 and 1 instead of 1 and 2.
    
    return binarized_array

 
def dilate_img (img):
    """
    This function dilates the objects of a binarised image and returns an array.
    Parameters:
    img: ndarray
        Variable containing the binarized image.
    """
    
    dilated_img = morphology.binary_dilation (img)

    
    return dilated_img

   
def remove_small_objects (img, min_size=64):
    """
    This function removes objects from a binarized image.
    Parameters:
    img: ndarray
        Variable containing the binarized image.
    min_size: int, optional
        The smallest allowable object size.
    """

    cleaned_img = morphology.remove_small_objects(img, min_size)

    return cleaned_img
