from readlif.reader import LifFile


file = LifFile('D:/estela/data/microscopy/leica_stellaris/20231011_e18_cd13_opn_arl13/20231011_e18_cd13_opn_arl13.lif')
img = file.get_image(2)


import napari
import numpy as np
import matplotlib.pyplot as plt
from naparimovie import Movie


    
    #The Z-stack images are piled up in their corresponding channels.
all_img = []
for c in range(img.channels):
    for z in range(img.nz):
        all_img.append(np.array(img.get_frame(z, 0, c, 0)))
    all_img_array = np.array(all_img)

    #The image format is reshaped by changing the order of variables. This is done so Napari is able to read the image correctly.
all_img_reshaped = np.reshape(all_img, (img.nz, img.channels, img.dims[0], img.dims[1]))
all_img_reshaped2 = all_img_reshaped.transpose(1, 0, 2, 3)
plt.imshow(all_img_reshaped2[0, 30, :, :])
    
    #Napari is executed and the image is visualized.
viewer = napari.Viewer()
#viewer.add_image(all_img_reshaped2, channel_axis= 0)
    
#movie = Movie(myviewer=viewer)

# movie.make_gif('gifmovie.gif') n              