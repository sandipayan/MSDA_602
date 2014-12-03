__author__ = 'sandipayannandi'

import csv
import random
import numpy as np



file="/Users/sandipayannandi/Documents/IS-602/Data/apple.2011.csv"
mc_price_list=[]
pct_change=[]

with open (file,"rb") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvreader)
    for row in csvreader:
        pct_change.append(float(row[2]))
        last_price=float(row[1])


pct_change_mean= np.mean(pct_change)
pct_change_std = np.std(pct_change)

range_length=100000

for i in range(range_length):
    last_price_mc=last_price
    for i in range(20):
        x=random.gauss(pct_change_mean,pct_change_std)
        last_price_mc=last_price_mc*(1+ x )
    mc_price_list.append(last_price_mc)

mc_one_pct= int(np.ceil(len(mc_price_list)*0.01))


mc_prediction=(sorted(mc_price_list)[mc_one_pct-1])

# print(sorted(mc_price_list)[range_length-1])

print ("Stock price will be above %f dollars after 20 days with a confidence level of 99 percentage."  %(mc_prediction) )




