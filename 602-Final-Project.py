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

hh_2001 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2001_HH_Seniors.csv', sep=',' ,quotechar='"' )
hh_2011 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2011_HH_Seniors.csv', sep=',' ,quotechar='"' )

hh_2001_2011=pd.concat([hh_2001,hh_2011], ignore_index=True)


    
pattern = re.compile(r"\ +\(\d+\)")
x=0

hh_2001_2011.insert(11, 'People_Cons_HH', '')
df_senior= pd.DataFrame(columns=('Census_Year' , 'State_Code' , 'State_Name', 'Region', 'People_Cons_HH' ,'No_Of_HH',  'Seniors_In_HH', 'Senior_Male' , 'Senior_Female' ))

for i in range(len(hh_2001_2011)):

     hh_2001_2011.People_Cons_HH[i]=1
     df_senior.loc[x] = ([hh_2001_2011.Census_Year[i],   hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_One[i].replace(',',''),       hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_One[i].replace(',','') ,       hh_2001_2011.Female_One[i].replace(',','') ] )
     hh_2001_2011.People_Cons_HH[i]=2
     df_senior.loc[x+1] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Two[i].replace(',',''),       hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Two[i].replace(',','') ,       hh_2001_2011.Female_Two[i].replace(',','') ] )
     hh_2001_2011.People_Cons_HH[i]=3
     df_senior.loc[x+2] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Three[i].replace(',',''),     hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Three[i].replace(',','') ,     hh_2001_2011.Female_Three[i].replace(',','') ] )
     hh_2001_2011.People_Cons_HH[i]=4
     df_senior.loc[x+3] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Four[i].replace(',',''),      hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Four[i].replace(',','') ,      hh_2001_2011.Female_Four[i].replace(',','') ] )
     hh_2001_2011.People_Cons_HH[i]=5
     df_senior.loc[x+4] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Five[i].replace(',',''),      hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Five[i].replace(',','') ,      hh_2001_2011.Female_Five[i].replace(',','') ] )
     hh_2001_2011.People_Cons_HH[i]=6
     df_senior.loc[x+5] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Six[i].replace(',',''),       hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Six[i].replace(',','') ,       hh_2001_2011.Female_Six[i].replace(',','') ] )
     hh_2001_2011.People_Cons_HH[i]=7
     df_senior.loc[x+6] = ([hh_2001_2011.Census_Year[i], hh_2001_2011.State_Code[i]  , re.sub(pattern,'',str(hh_2001_2011.State_Name[i])).replace('State - ',''), hh_2001_2011.Region[i],hh_2001_2011.People_Cons_HH[i], hh_2001_2011.Households_Seven_Plus[i].replace(',',''),hh_2001_2011.Seniors_In_HH[i].replace('None','0') , hh_2001_2011.Male_Seven_Plus[i].replace(',','') ,hh_2001_2011.Female_Seven_Plus[i].replace(',','') ] )

     x=x+7

print(len(df_senior))
df_senior.to_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/concat.csv', sep=',',quotechar='"' )


# Scrub data for population
################################

hh_pop_2001 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2001_HH_Population.csv', sep=',' ,quotechar='"' )
hh_pop_2011 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2011_HH_Population.csv', sep=',' ,quotechar='"' )

hh_pop_2001_2011=pd.concat([hh_pop_2001,hh_pop_2011], ignore_index=True)






print(len(df_senior))
df_senior.to_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/concat.csv', sep=',',quotechar='"' )







# df.to_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/result.csv', sep=',')
#
# df_old = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/result.csv' , sep=',' , quotechar='"' )
#
# df_pop= pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2001_HH_Population.csv' , sep=',' , quotechar='"' )


# print(len(df_pop))


