__author__ = 'sandipayannandi'

import csv
import Tkinter
import tkFileDialog
import sys
sys.path.append("/Users/sandipayannandi/anaconda/lib/python2.7/site-packages/")
import numpy as np
import scipy
import timeit
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



# Linear Regression Calculation

def LinearReg(bo,br):

    """
    This function  will take two lists x & y  and show the linear regression equation
    for those two lists od data
    :param x: This is the first set of data list , for this program is the BodyWeight
    :param y: This is the second set of data list , for this program is the BrainWeight
    :return:  A linear equation of the form Y = bX + a , where 'b' is the slope and 'a'
              is a constant called 'Intercept', 'Y' is BrainWeight and 'X' is BodyWeight

    Regression Equation(y) = a + bx
    Slope(b)=  ( N* sum(XY) - sum(X) * sum(Y) )  / ( N* sum(X^2) - ( sum(X) ) ^2 )
    Intercept(a) = ( Sum(Y)  - b * sum(X) )  / N

    b = The slope of the regression line
    a = The intercept point of the regression line and the y axis.
    N = Number of values or elements

    """

    N= len(bo)

    sum_XY=0
    sum_X=0
    sum_Y=0
    sum_X2=0



    for i in range(0,N):
        sum_XY=sum_XY + bo[i]*br[i]
        sum_X= sum_X + bo[i]
        sum_Y= sum_Y + br[i]
        sum_X2=sum_X2+ bo[i]*bo[i]



    b=  ( N* sum_XY - sum_X * sum_Y )  / ( N* sum_X2 - ( sum_X * sum_X)  )
    a = ( sum_Y  - b * sum_X )  / N



    return("Equation: Manual Derivation Y = %.4f X +%.2f " %(b,a))



# plt.plot(bo, br)
# plt.show()



#### Linear regression calculation using Scipy


def LinearRegScipy(bo,br):
    from scipy import stats
    slope, intercept, r_value,p_value, std_err= stats.linregress(bo,br)
    return("Equation: Scipy Derivation Y = %.4f X +%.2f " %(slope,intercept))


## Curve fitting using Scipy

def LinReg(x,slope,intercept):
    return(slope * x + intercept)



if __name__=="__main__":
    root=Tkinter.Tk()
    root.withdraw()
    file=tkFileDialog.askopenfilename(parent=root)

    bo=[]
    br=[]

    with open (file,"rb") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvreader)

        for row in csvreader:
            bo.append(float(row[1]))
            br.append(float(row[2]))


    if ( all(isinstance(item, (float,int)) for item in bo) ) != True:
        print (" Body column does not have all numeric values" )
        exit
    elif ( all(isinstance(item, (float,int)) for item in br) ) != True:
        print (" Brain column does not have all numeric values" )
        exit
    elif len(bo) != len(br):
        print("Body & Brain does not have the same length of values")





if __name__=='__main__':
    from timeit import Timer
    x=LinearReg(bo,br)
    print x
    t = Timer(lambda: LinearReg(bo,br))
    print "Timing: Manual Derivation. %d loops in %f seconds " %( 10000, t.timeit(number=10000))

    y=LinearRegScipy(bo,br)
    print y
    t = Timer(lambda: LinearRegScipy(bo,br))
    print "Timing: Scipy Derivation. %d loops in %f seconds " %( 10000, t.timeit(number=10000))


    t = np.linspace(0,5,50)
    temp=LinReg(t,0.0043,266.32)
    noisy = temp + 0.5*np.random.normal(size=len(temp))
    fitParams, fitCovariances = curve_fit(LinReg, t, noisy)
    # print(len(fitParams))
    print ' fit coefficients:\n', fitParams
    print ' Covariance matrix:\n', fitCovariances


# plt.plot(fitParams,LinReg(fitParams, 0.0043,266.32))
#
# plt.show()



# Equation: Manual Derivation Y = 0.0043 X +266.32
# Timing: Manual Derivation. 10000 loops in 0.208280 seconds
# Equation: Scipy Derivation Y = 0.0043 X +266.32
# Timing: Scipy Derivation. 10000 loops in 1.376707 seconds
#  fit coefficients:
# [  7.69217344e-02   2.66108058e+02]
#  Covariance matrix:
# [[ 0.00260145 -0.00650361]
#  [-0.00650361  0.02189992]]
#
# Process finished with exit code 0