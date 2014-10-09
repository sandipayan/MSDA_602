__author__ = 'sandipayannandi'

import csv
import Tkinter
import tkFileDialog

def LinearReg():

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



print("Linear regression equation is: Y = %.4f X +%.2f " %(b,a))














