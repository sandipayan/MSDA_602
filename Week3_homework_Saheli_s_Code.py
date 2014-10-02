import Tkinter
import tkFileDialog
import csv
import re
class CarEvaluation:
    'A simple class that represents a car evaluation'
    carCount=0;
def __init__(self, car):
    self.car = car
    self.buying = car[0]
    self.maint = car[1]
    self.doors = car[2]
    self.persons = car[3]
    self.lug_boot = car[4]
    self.safety = car[5]
    if(self.buying!='vhigh' and self.buying!='high' and self.buying!='med' and self.buying!='low'):
        raise ValueError('Wrong entry in buying')
    if(self.maint!='vhigh' and self.maint!='high' and self.maint!='med' and self.maint!='low'):
        raise ValueError('Wrong entry in Maintenance')
    if(self.doors!='2' and self.doors!='3' and self.doors!='4' and self.doors!='5more'):
        raise ValueError('Wrong entry in Doors')
    if(self.persons!='2' and self.persons!='4' and self.persons!='more'):
        raise ValueError('Wrong entry in Persons')
    if(self.lug_boot!='small' and self.lug_boot!='med' and self.lug_boot!='big'):
        raise ValueError('Wrong entry in Lug boot')
    if(self.safety!='high' and self.safety!='med' and self.safety!='low'):
        raise ValueError('Wrong entry in Safety')

    self.__class__.carCount+=1

def showCars(self):
    print "The car's Buying:%s, maint:%s, lug_boot:%s, doors:%s, safety:%s, persons:%s" %(self.buying, self.maint, self.lug_boot, self.doors, self.safety, self.persons)

## function that sorts the list of cars by safety type
def sortbysafety(carList, sortType):
    tmpList = []
    for car in carList:
        if car.safety == "high":
            tmpList.append((car, 3))
        elif car.safety == "med":
            tmpList.append((car, 2))
        elif car.safety == "low":
            tmpList.append((car, 1))
#sort list using safety
    if sortType == "asc":
        tmpList = sorted(tmpList, key=lambda car: car[1])
    elif sortType == "des":
        tmpList = sorted(tmpList, key=lambda car: car[1], reverse=True)
    carList = []
    for tmpVal in tmpList:
        carList.append(tmpVal[0])
        return carList
## function that sorts the list of cars by maintenance type
def sortbymaintenance(carList, sortType):
    tmpList = []
    for car in carList:
        if car.maint == "vhigh":
            tmpList.append((car, 4))
        elif car.maint == "high":
            tmpList.append((car, 3))
        elif car.maint == "med":
            tmpList.append((car, 2))
        elif car.maint == "low":
            tmpList.append((car, 1))
#sort list using maintenance
    if sortType == "asc":
        tmpList = sorted(tmpList, key=lambda car: car[1])
    elif sortType == "des":
        tmpList = sorted(tmpList, key=lambda car: car[1], reverse=True)
    carList = []
    for tmpVal in tmpList:
        carList.append(tmpVal[0])
    return carList

## function that sorts the list of cars by doors

def sortbydoors(carList, sortType):
#sort list using doors
    if sortType == "asc":
        carList = sorted(carList, key=lambda car: car.doors)
    elif sortType == "des":
        carList = sorted(carList, key=lambda car: car.doors, reverse=True)
        return carList

# This is the main of the program.

if __name__ == "__main__":
## block that reads a csv file ##
    root=Tkinter.Tk()
    root.withdraw()
    try:
        filename=tkFileDialog.askopenfilename(parent=root)
        f = open(filename,"rb")
        reader = csv.reader(f, delimiter = ",")
        carList=[]
        for row in reader:
            try:
                car = CarEvaluation(row)
            except ValueError, e:
                print e
            continue
        else:
            carList.append(car)
        f.close()
        ## ------------------------##
        ## block that inputs the car List and sort them by safety and prints out the first 10 rows from the sorted list
        sortedCarList = sortbysafety(carList, "des")
        print "------Sorted by safety ------"
        for car in sortedCarList[1:10]:
            car.showCars()
        ## block that inputs the car List and sort them by maintenance and prints out the last 15 rows from the sorted list
        sortedCarList = sortbymaintenance(carList, "asc")
        print "------Sorted by maintenance ------"
        for car in sortedCarList[-15:]:
            car.showCars()
        ## block that inputs the car List and sort them by doors and prints out list whose safety, maintenanace and buying are high or vhigh
        print "------Sorted by doors with filtered list ------"
        sortedCarList = sortbydoors(carList, "asc")
        filteredList = []
        pattern = 'high'
        for car in carList:
            if re.search(pattern,car.buying) and re.search(pattern, car.maint)and re.search(pattern, car.safety) :
                filteredList.append(car)
        car.showCars()
        ### Saves the list to a file ###
        print "Select a file to save data--"
        filename=tkFileDialog.askopenfilename(parent=root)
        f = open(filename,"w")
        for car in filteredList:
            f.write (str(car.buying)+','+ str(car.maint)+','+ str(car.doors)+','+ str(car.persons)+','+ str(car.lug_boot)+','+ str(car.safety)+'\n')
        f.close()

    except Exception, e:
        print "Caught: ",e
        print "Error occurred, exiting gracefully"
