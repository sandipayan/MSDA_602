__author__ = 'sandipayannandi'

import sys
sys.path.append("/Users/sandipayannandi/anaconda/lib/python2.7/site-packages/")

import pandas as pd
import numpy as np
import re
import random
import matplotlib.pyplot as plt


#######################

# 2011: Household and population data extracted from :
# http://www.censusindia.gov.in/2011census/hh-series/hh01.html
# 2001:
#http://www.censusindia.gov.in/(S(5ccvsj45jl3zxj555acdx345))/DigitalLibrary/MFTableSeries.aspx

########################


## Scrub data for seniors

# hh_2001 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2001_HH_Seniors.csv', sep=',' ,quotechar='"' )
# hh_2011 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2011_HH_Seniors.csv', sep=',' ,quotechar='"' )
#
# hh_2011['Region']=hh_2011['Region'].map(lambda x:str(x).upper() )
#
# hh_2001_2011=pd.concat([hh_2001,hh_2011], ignore_index=True)
#
#
# pattern = re.compile(r"\ +\(\d+\)")
# x=0
#
# hh_2001_2011.insert(11, 'People_Cons_HH', '')
# df_senior= pd.DataFrame(columns=('Census_Year' , 'State_Code' , 'State_Name', 'Region', 'People_Cons_HH' ,'No_Of_HH',  'Seniors_In_HH', 'Senior_Male' , 'Senior_Female' ))
#
# for i in range(len(hh_2001_2011)):
#
#      hh_2001_2011.People_Cons_HH[i]=1
#      df_senior.loc[x] = ([hh_2001_2011.Census_Year[i],   hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ','') , hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_One[i].replace(',',''),       hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_One[i].replace(',','') ,       hh_2001_2011.Female_One[i].replace(',','') ] )
#      hh_2001_2011.People_Cons_HH[i]=2
#      df_senior.loc[x+1] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Two[i].replace(',',''),       hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Two[i].replace(',','') ,       hh_2001_2011.Female_Two[i].replace(',','') ] )
#      hh_2001_2011.People_Cons_HH[i]=3
#      df_senior.loc[x+2] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Three[i].replace(',',''),     hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Three[i].replace(',','') ,     hh_2001_2011.Female_Three[i].replace(',','') ] )
#      hh_2001_2011.People_Cons_HH[i]=4
#      df_senior.loc[x+3] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Four[i].replace(',',''),      hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Four[i].replace(',','') ,      hh_2001_2011.Female_Four[i].replace(',','') ] )
#      hh_2001_2011.People_Cons_HH[i]=5
#      df_senior.loc[x+4] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Five[i].replace(',',''),      hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Five[i].replace(',','') ,      hh_2001_2011.Female_Five[i].replace(',','') ] )
#      hh_2001_2011.People_Cons_HH[i]=6
#      df_senior.loc[x+5] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Six[i].replace(',',''),       hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Six[i].replace(',','') ,       hh_2001_2011.Female_Six[i].replace(',','') ] )
#      hh_2001_2011.People_Cons_HH[i]=7
#      df_senior.loc[x+6] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Seven_Plus[i].replace(',',''),hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Seven_Plus[i].replace(',','') ,hh_2001_2011.Female_Seven_Plus[i].replace(',','') ] )
#
#      x=x+7
#
# print(len(df_senior))
# df_senior.to_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/Seniors.csv', sep=',',quotechar='"' )


df_senior = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/Seniors.csv', sep=',' ,quotechar='"' )


# Scrub data for population
################################

# hh_pop_2001 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2001_HH_Population.csv', sep=',' ,quotechar='"' )
# hh_pop_2011 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2011_HH_Population.csv', sep=',' ,quotechar='"' )
#
# hh_pop_2011['Region']=hh_pop_2011['Region'].map(lambda x:str(x).upper() )
#
#
#
# hh_pop_2001_2011=pd.concat([hh_pop_2001,hh_pop_2011], ignore_index=True)
#
# x=0
#
# df_pop= pd.DataFrame(columns=('Census_Year' , 'State_Code' , 'State_Name', 'Region', 'No_Of_HH' ,'Population' , 'Avg_HH_Population' ))
#
# for i in range(len(hh_pop_2001_2011)):
#
#       df_pop.loc[x] = ([str(hh_pop_2001_2011.Census_Year[i]).replace(',',''),   hh_pop_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_pop_2001_2011.State_Name[i])).replace('State - ','').replace('Union Territory - ',''), hh_pop_2001_2011.Region[i], str(hh_pop_2001_2011.No_Of_HH[i]).replace(',',''), str(hh_pop_2001_2011.Population[i]).replace(',',''),   hh_pop_2001_2011.Avg_HH_Population[i]  ] )
#       x=x+1
#
#
# df_pop.to_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/Population.csv', sep=',',quotechar='"' )
#

df_pop = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/Population.csv', sep=',' ,quotechar='"' )



######################################################
# 2001 state wise old vs Young population
######################################################

def state_wise_old_vs_young(yr):

    x= df_senior[[  'State_Name', 'Senior_Male' , 'Senior_Female']]   [ ( df_senior['Seniors_In_HH']== "Total")  & ( df_senior['Region']== "TOTAL")  & ( df_senior['Census_Year']== yr) ]
    x=x.groupby('State_Name', as_index=False).sum()
    x['sum_old']= x['Senior_Male'] + x['Senior_Female']
    x=x[[ 'State_Name','sum_old'  ]].sort( ['sum_old'], ascending=[0] )


    y= df_pop[[  'State_Name', 'Population']]   [  ( df_pop['Region']== "TOTAL")  & ( df_pop['Census_Year']== yr) ]
    y=y.sort( ['Population'], ascending=[0] )


    z=pd.merge(x,y, on='State_Name')
    z['sum_young']= z['Population'] - z['sum_old']
    z['Pct_old']=  z['sum_old'] / z['Population'] *100

    z['Pct_old']=z['Pct_old'].map(lambda x: round(x,2)).astype(str) + "%"
    print(z)



    x=np.arange(len(z['State_Name']))
    Old=z['sum_old']
    Young=z['sum_young']

    #print(z)

    p1=plt.bar(x,Old,color='r',bottom=Young)
    p2=plt.bar(x,Young,color='y')
    tkname=z['State_Name'].tolist()
    plt.xticks(x, tkname,rotation=45,ha='right' )
    plt.legend( (p1[0], p2[0]), ('Old', 'Young') )
    plt.title("Old & Young distribution - Census Year "+ str(yr))


    def autolabel(rects):
        name=z['Pct_old'].tolist()
        for ii,rect in enumerate(rects):
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., (height + 120000000), '%s'% (name[ii]),
                    ha='center', va='bottom',rotation=90)

    autolabel(p2)

    plt.show()


######################################################
# 2011 state wise old vs total population
######################################################
state_wise_old_vs_young(2001)
state_wise_old_vs_young(2011)














