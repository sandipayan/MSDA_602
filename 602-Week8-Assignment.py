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




#
#
# Finding number of objects & center of mass for ********   circles.png
#
# Number of labelled objects:  5
# ('Center of mass is : ', [(124.23003300330033, 369.54257425742577), (150.10358031782499, 522.28623396515411), (203.46548117154811, 212.50156903765691), (299.44032509463369, 361.82565130260519), (366.85278886153321, 188.78334323796588)])
#
#
# Finding number of objects & center of mass for ********   objects.png
# Number of labelled objects:  8
# ('Center of mass is : ', [(74.390596026490073, 508.01324503311258, 1.0), (160.40598025853879, 182.38760170156527, 1.0), (149.06617647058823, 410.12249687108886, 1.0), (370.8319420879991, 418.00357425630585, 1.0), (282.87421383647796, 259.83018867924528, 1.0), (326.32797202797201, 184.70489510489512, 1.0), (399.20610687022901, 94.312977099236647, 1.0), (436.45785123966942, 172.13911845730027, 1.0)])
#
#
# Finding number of objects & center of mass for ********   peppers.png
# Number of labelled objects:  26
# ('Center of mass is : ', [(236.02262814765285, 249.95582648207528, 1.7226171299180888), (29.592592592592592, 113.92592592592592, 3.0), (30.086956521739129, 199.08695652173913, 3.0), (38.0, 201.0, 3.0), (53.127868852459017, 221.70819672131148, 3.0), (50.0, 199.5, 3.0), (220.58227292672225, 12.593242650285212, 2.2838964458095656), (321.14727041895895, 496.99661447312741, 1.9763013118916632), (316.5, 70.0, 3.0), (326.0, 467.0, 3.0), (331.75555555555553, 50.466666666666669, 3.0), (329.28571428571428, 65.214285714285708, 3.0), (329.0, 36.5, 3.0), (349.11883408071748, 59.647982062780272, 2.688340807174888), (344.34482758620692, 43.517241379310342, 3.0), (357.0, 73.0, 3.0), (391.57894736842104, 16.131578947368421, 3.0), (403.78787878787881, 439.15151515151513, 2.7878787878787881), (419.69230769230768, 313.03846153846155, 3.0), (472.06540627514079, 459.55245374094932, 1.8022526146419953), (483.94444444444446, 391.05555555555554, 3.0), (492.92307692307691, 297.61538461538464, 3.0), (494.88235294117646, 310.02941176470586, 3.0), (504.66005665722378, 366.39603399433429, 1.836827195467422), (505.78431372549022, 427.70588235294116, 2.1568627450980391), (507.71673819742489, 299.71244635193131, 3.0)])
#
#
