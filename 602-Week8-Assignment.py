__author__ = 'sandipayannandi'

import sys
sys.path.append("/Users/sandipayannandi/anaconda/lib/python2.7/site-packages/")


import numpy as np
from scipy import misc,ndimage



def picture_img(picture,sigma,threshold_val):

    print("Finding number of objects & center of mass for ********   " + picture )

    objects= misc.imread("/Users/sandipayannandi/Documents/IS-602/Data/images/"+ picture)

    objects_filtered = ndimage.gaussian_filter(objects,sigma)

    if threshold_val==1:
        thres = objects_filtered > 100 #objects_filtered.mean()
    elif threshold_val==2:
        thres = objects_filtered > objects_filtered.mean()

    misc.imsave("filtered_" + picture , thres)

    labled_array, num_features = ndimage.label(thres)

    #print(labled_array)
    print( "Number of labelled objects:  %d"   %(num_features) )
    print ( "Center of mass is : " , ndimage.measurements.center_of_mass(thres, labled_array, range(1, num_features+1 )))





if __name__=="__main__":
    picture_img("circles.png",1.5, 1)
    picture_img("objects.png",8,2)
    picture_img("peppers.png",1.95,2)








