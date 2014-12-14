__author__ = 'sandipayannandi'

import pandas as pd
import numpy as np
import re
import random

hh_2001 = pd.read_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/2001_HH.csv', sep=',' ,quotechar='"' )


print(len(hh_2001))



hh_2001.insert(11, 'People_Cons_HH', '')
df= pd.DataFrame(columns=('Census_Year' , 'State_Code' , 'State_Name', 'Region', 'People_Cons_HH' ,'No_Of_HH',  'Seniors_In_HH', 'Senior_Male' , 'Senior_Female' ))

x=0

for i in range(len(hh_2001)):
     hh_2001.People_Cons_HH[i]=1
     df.loc[x] = ([hh_2001.Census_Year[i],   hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_One[i],       hh_2001.Seniors_In_HH[i] , hh_2001.Male_One[i] ,       hh_2001.Female_One[i] ] )
     hh_2001.People_Cons_HH[i]=2
     df.loc[x+1] = ([hh_2001.Census_Year[i], hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_Two[i],       hh_2001.Seniors_In_HH[i] , hh_2001.Male_Two[i] ,       hh_2001.Female_Two[i] ] )
     hh_2001.People_Cons_HH[i]=3
     df.loc[x+2] = ([hh_2001.Census_Year[i], hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_Three[i],     hh_2001.Seniors_In_HH[i] , hh_2001.Male_Three[i] ,     hh_2001.Female_Three[i] ] )
     hh_2001.People_Cons_HH[i]=4
     df.loc[x+3] = ([hh_2001.Census_Year[i], hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_Four[i],      hh_2001.Seniors_In_HH[i] , hh_2001.Male_Four[i] ,      hh_2001.Female_Four[i] ] )
     hh_2001.People_Cons_HH[i]=5
     df.loc[x+4] = ([hh_2001.Census_Year[i], hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_Five[i],      hh_2001.Seniors_In_HH[i] , hh_2001.Male_Five[i] ,      hh_2001.Female_Five[i] ] )
     hh_2001.People_Cons_HH[i]=6
     df.loc[x+5] = ([hh_2001.Census_Year[i], hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_Six[i],       hh_2001.Seniors_In_HH[i] , hh_2001.Male_Six[i] ,       hh_2001.Female_Six[i] ] )
     hh_2001.People_Cons_HH[i]=7
     df.loc[x+6] = ([hh_2001.Census_Year[i], hh_2001.State_Code[i]  , hh_2001.State_Name[i], hh_2001.Region[i],hh_2001.People_Cons_HH[i], hh_2001.Households_Seven_Plus[i],hh_2001.Seniors_In_HH[i] , hh_2001.Male_Seven_Plus[i] ,hh_2001.Female_Seven_Plus[i] ] )

     x=x+7

print(len(df))

df.to_csv('/Users/sandipayannandi/Documents/IS-602/602-Final-Project/result.csv', sep=',')



print(df.head(10))