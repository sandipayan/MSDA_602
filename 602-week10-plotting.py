import numpy as np
import sys
import re
sys.path.append("/Users/sandipayannandi/anaconda/lib/python2.7/site-packages/")
import matplotlib.pyplot as plt
import csv
from scipy import misc,ndimage

def bar_plot():

    f=open("/Users/sandipayannandi/Documents/IS-602/Data/cars.data.csv", "rU")
    lines = f.readlines()
    f.close()

    buying_price=[]
    maint_price=[]
    doors=[]
    safety=[]


    for i in range(0,len(lines)):
       buying_price.append( (lines[i].split(","))[0])
       maint_price.append( lines[i].split(",") [1] )
       doors.append( lines[i].split(",") [2] )
       safety.append( lines[i].split(",") [5] )


    def get_y(param):
        d={i:param.count(i) for i in param}
        y=d.values()
        return(y)


    plt.figure('car.csv attributes' , tight_layout= True)

    plt.subplot(221)
    y=get_y(buying_price)
    x = np.arange(len(y))
    plt.bar(x,y)
    plt.xlabel('Buying Price')
    plt.ylabel('Frequency')
    plt.title('Buy')


    plt.subplot(222)
    y=get_y(maint_price)
    x = np.arange(len(y))
    plt.bar(x,y)
    plt.xlabel('Maintenance Price')
    plt.ylabel('Frequency')
    plt.title('Maintenance')


    plt.subplot(223)
    y=get_y(doors)
    x = np.arange(len(y))
    plt.bar(x,y)
    plt.xlabel('Doors')
    plt.ylabel('Frequency')
    plt.title('Door')

    plt.subplot(224)
    y=get_y(safety)
    x = np.arange(len(y))
    plt.bar(x,y)
    plt.xlabel('Safety Ratings')
    plt.ylabel('Frequency')
    plt.title('Safety')


    plt.show()



def linreg_plot():

    file="/Users/sandipayannandi/Documents/IS-602/Data/brainandbody.csv"

    bo=[]
    br=[]

    with open (file,"rb") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvreader)

        for row in csvreader:
            bo.append(float(row[1]))
            br.append(float(row[2]))


    x = bo
    y = br # 10, not 9, so the fit isn't perfect

    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) # fit_fn is now a function which takes in x and returns an estimate for y

    plt.figure('brainbody')
    plt.title('Linear Regression with Scatter Plot')
    plt.xlabel('Body Weight')
    plt.ylabel('Brain Weight')
    plt.plot(x,y, 'yo', x, fit_fn(x), '-')
    # plt.xlim(0, 5)
    # plt.ylim(0, 12)
    plt.show()



def obj_center():
    objects= misc.imread("/Users/sandipayannandi/Documents/IS-602/Data/images/objects.png")

    com=[(74.390596026490073, 508.01324503311258), (160.40598025853879, 182.38760170156527), (149.06617647058823, 410.12249687108886), (370.8319420879991, 418.00357425630585), (282.87421383647796, 259.83018867924528), (326.32797202797201, 184.70489510489512), (399.20610687022901, 94.312977099236647), (436.45785123966942, 172.13911845730027) ]

    plt.figure('Objects')
    plt.title('Center of Mass of Objects')
    plt.imshow(objects)

    for l in com:
        plt.scatter (l[1],l[0], color='r')

    plt.show()



def hourly_view_cnt():

    plt.figure('hourly_view_cnt')
    plt.title('Hourly View Count')
    plt.xlabel('Hours')
    plt.ylabel('Count Of Views')
    #plt.tick_params(direction='out', length=6, width=2, colors='r')
    hourly_cnt={00:684,01:434,02:399,03:248,4:347,5:374,6:303,7:846,8:1994,9:3096,10:3209,11:3820,12:3827,13:4391,14:4716,15:4284,16:4042,17:2793,18:1820,19:1493,20:1310,21:1015,22:1117,23:1186 }
    my_xticks=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    plt.xticks(hourly_cnt.keys(), my_xticks)

    plt.plot(hourly_cnt.keys(), hourly_cnt.values())
    plt.plot(hourly_cnt.keys(), hourly_cnt.values(),'r.',markersize=8)
    plt.show()







if __name__=='__main__':
    bar_plot()
    linreg_plot()
    obj_center()
    hourly_view_cnt()



