__author__ = 'sandipayannandi'

import sys
sys.path.append("/Users/sandipayannandi/anaconda/lib/python2.7/site-packages/")

import pandas as pd
import numpy as np
import re
import random
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.cm as cm
import shapefile
from pysal.esda.mapclassify import Natural_Breaks as nb
from matplotlib.colors import Normalize
from bokeh.plotting import *


df_map=pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/Single_Living_Alone.csv', sep=',' ,quotechar='"' )



# Calculate Jenks natural breaks for density
breaks = nb(
    df_map['pct_old_living_alone'],
    initial=0,
    k=5)


jb = pd.DataFrame({'jenks_bins': breaks.yb}, index=df_map['pct_old_living_alone'].index)
df_map = df_map.join(jb)


cmap = plt.get_cmap('Blues')


norm = Normalize()
palette=cmap(norm(df_map['jenks_bins'].values))

palette_hex=[]

for i in range(len(palette)):
    palette_hex.append("#%02x%02x%02x" % (   tuple(palette[i])[0]*255, tuple(palette[i])[1]*255, tuple(palette[i])[2]*255))

df_map['Palette']=pd.Series(palette_hex)



def getParts ( shapeObj ):

    points = []

    num_parts = len( shapeObj.parts )
    end = len( shapeObj.points ) - 1
    segments = list( shapeObj.parts ) + [ end ]

    for i in range( num_parts ):
        points.append( shapeObj.points[ segments[i]:segments[i+1] ] )

    return points


def getDict ( state_name, shapefile ):

    stateDict = {state_name: {} }

    shp = []
    points = []


    # Select only the records representing the
    # "state_name" and discard all other
    for i in shapefile.shapeRecords( ):

        if i.record[2] == state_name:
            shp.append(i.shape)

    for j in shp:
        for i in getParts(j):
            points.append(i)


    lat = []
    lng = []
    for i in points:
        lat.append( [j[0] for j in i] )
        lng.append( [j[1] for j in i] )


    stateDict[state_name]['lat_list'] = lat
    stateDict[state_name]['lng_list'] = lng

    return stateDict




# Read the ShapeFile, this is downloaded from a website
dat = shapefile.Reader("/Users/sandipayannandi/anaconda/lib/python2.7/site-packages/India_State/India_State.shp")


# Create a Unique List of States (Administrative Regions)
states = set([i[2] for i in dat.iterRecords()])


# Create the Plot, using bokeh, which is kind of new


# use output_file while in PyCharm, use output_notebook() in the Ipython notebook

output_file("india_states.html")

#output_notebook()

hold()

TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
p=figure(title="Percentage of Seniors Living Alone", tools=TOOLS, plot_width=800, plot_height=650)


bins=sorted(list(df_map['jenks_bins'].unique()))

x0 = [1, 2, 3, 4, 5]

for i in bins:
    pct_min=df_map['pct_old_living_alone'][ df_map['jenks_bins']==i ].min()
    pct_max=df_map['pct_old_living_alone'][ df_map['jenks_bins']==i ].max()
    map_col=df_map['Palette'][ df_map['jenks_bins']==i ].unique()
    map_col=str(map_col).strip('[').strip(']').strip("'")
    p.circle(x0, x0, legend=str(pct_min) + "-" + str(pct_max)+"%" ,fill_color= "%s"%map_col )


print(df_map)



for state_name in states:
    col= df_map['Palette'][( df_map['State_Name']== state_name.upper())].to_string()

    if col.find("#") == -1:
        next(states.__iter__())

    else:
        col=col.split()[1]
        data = getDict(state_name,dat)
        patches(data[state_name]['lat_list'], data[state_name]['lng_list'], \
                fill_color= "%s"%col , line_color="black")



show()




