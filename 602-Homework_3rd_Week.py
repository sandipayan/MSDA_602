
import re

f=open("/users/sandipayannandi/Documents/IS-602/Week3/cars.data.csv", "rU")
lines = f.readlines()
f.close()

buying_price=[]
maint_price=[]
doors=[]
persons=[]
lug_boot=[]
safety=[]
n_buying_price=[]
n_safety=[]
n_maint=[]


def map(input):
    if (input=='vhigh' or input=='v-high' ):
        return 1
    elif (input=='high' or input=='big'):
        return 2
    elif (input=='med'):
        return 3
    elif (input=='low' or input=='small'):
        return 4
    else:
        return 5


for i in range(0,len(lines)):
   buying_price.append( (lines[i].split(","))[0])
   maint_price.append( lines[i].split(",") [1] )
   doors.append( lines[i].split(",") [2] )
   persons.append( lines[i].split(",") [3] )
   lug_boot.append( lines[i].split(",") [4] )
   safety.append( lines[i].split(",") [5] )

   n_buying_price.append( map ( (lines[i].split(","))[0]) )
   n_safety.append( map ( (lines[i].split(","))[5]) )
   n_maint.append( map ( (lines[i].split(","))[1]) )


if(set(buying_price) != set(['high', 'med',  'low', 'vhigh'])):
    raise ValueError('Wrong entry in buying price')
if(set(maint_price) != set(['high', 'med', 'vhigh', 'low'])):
    raise ValueError('Wrong entry in maint price')
if(set(doors) != set(['5more', '3', '2', '4'])):
    raise ValueError('Wrong entry in doors')
if(set(persons) != set(['2', '4', 'more'])):
    raise ValueError('Wrong entry in persons')
if(set(lug_boot) != set(['small', 'med', 'big'])):
    raise ValueError('Wrong entry in lug boot')
if(set(safety) != set(['high', 'med', 'low'])):
    raise ValueError('Wrong entry in safety')



# print the top 10 rows of the data sorted by 'safety' in descending order
sorted_safety = sorted(range(len(n_safety)), key=lambda k: n_safety[k])

for i in range(0,10):
    print (lines[sorted_safety[i]])


print("******************************************")
# print the bottom 15 rows of the data sorted by 'maint' in ascending order, i.e first 15 rows in descending order
sorted_maint = sorted(range(len(n_maint)), key=lambda k: n_maint[k])

for i in range(0,15):
    print (lines[sorted_maint[i]])

print("******************************************")
# Print all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order

pattern=re.compile('high|vhigh')

f_buy = [i for i in range(0,len(buying_price)) if buying_price[i]=='vhigh' or buying_price[i] =='high']
f_maint  = [x for i, x in enumerate(f_buy)   if re.match(pattern, maint_price[x])]
f_safety  = [x for i, x in enumerate(f_maint)   if re.match(pattern, safety[x])]


f_door={}

for i,x in enumerate(f_safety):
    f_door[x]=doors[x]

for key, value in sorted(f_door.iteritems(), key=lambda (k,v): (v,k)):
    print(lines[key])

# save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.
print("******************************************")


pattern=re.compile('4|more')

f_buy_w = [i for i in range(0,len(buying_price)) if buying_price[i] =='high']
f_maint_w  = [x for i, x in enumerate(f_buy_w)   if re.match('med', maint_price[x])]
f_doors_w  = [x for i, x in enumerate(f_maint_w)   if re.match('4', doors[x])]
f_persons_w  = [x for i, x in enumerate(f_doors_w)   if re.match(pattern, persons[x])]

f=open("/users/sandipayannandi/Documents/IS-602/Week3/output.txt", "w")

for i,x in enumerate(f_persons_w):
    f.write(lines[x])

f.close()


