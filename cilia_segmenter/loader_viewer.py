#In this script, .lif images from the Leica Stellaris microscope are loaded and opened in the 3D viewer Napari. Images are reconstructed from the .lif file by combining the channels and their respective z-stacks.
from readlif.reader import LifFile
import numpy as np
import matplotlib.pyplot as plt
    
def lifloader(path, index):
    """
    This function loads the .lif file experiment by indicating the path where the file is found and the image index (position in the folder). 
    The function reconstructs the image by using its channels and z stack. It returns an ndarray.
    Parameters:
    path: path
        Path where the .lif file is found.
    index: integer
        Indicates the image to be later opened from the experiment file (starting from 0).
        """
    file = LifFile(path)
    img = file.get_image(index)
    
    #The Z-stack images are piled up in their corresponding channels and the image is converted to an array.
    all_img = []
    for c in range(img.channels):
        for z in range(img.nz):
            all_img.append(np.array(img.get_frame(z, 0, c, 0)))
    all_img_array = np.array(all_img)
    
    #The image format is reshaped by changing the order of variables. This is done so Napari is able to read the image correctly.
    all_img_reshaped = np.reshape(all_img_array, (img.nz, img.channels, img.dims[0], img.dims[1]))
    all_img_reshaped2 = all_img_reshaped.transpose(1, 0, 2, 3)
    plt.imshow(all_img_reshaped2[0, 30, :, :])
    
    return all_img_reshaped2


import napari

def napari_viewer(img):
    """
    This function opens the different channels as separate images in Napari.
    Parameters:
    img: ndarray
        Variable containing the loaded image of interest.
        The dimensions of the image can be indicated. In img [:,:,:,:], index 0 corresponds to the channels and index 1 corresponds to the z stack.
    """
 
    #Napari is executed and the image is visualized.
    viewer = napari.Viewer()
    viewer.add_image(img, channel_axis=0)

def napari_viewer_all_in_one(img):
    """
    This function opens all the channels as one image in Napari. It is useful when a single channel is needed.
    Parameters:
    img: ndarray
        Variable containing the loaded image of interest.
        The dimensions of the image can be indicated. In img [:,:,:,:], index 0 corresponds to the channels and index 1 corresponds to the z stack.
    """
    
    #Napari is executed and the image is visualized.
    viewer = napari.Viewer()
    viewer.add_image(img)
    
    
#D:/estela/data/microscopy/leica_stellaris/S