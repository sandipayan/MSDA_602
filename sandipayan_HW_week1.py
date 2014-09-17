#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    input_list=list(input)
    op_list=list([input_list[0]])
    input_list.remove(input_list[0])
    while len(input_list)>0:
        i=-1
        inserted=False
        for elements in op_list:
            i=i+1
            # had to use this as op_list.index(elements) does not work properly when there are duplicate elements
            if len(op_list)>1 and i < len(op_list)-1 and inserted==False:
                if op_list[i] <= input_list[0] <= op_list[i+1]:
                    op_list.insert(i+1,input_list[0])
                    input_list.remove(input_list[0])
                    inserted=True


        if inserted == False:
            if input_list[0] <= op_list[0]:
                op_list.insert(0,input_list[0])
            else:
                op_list.append(input_list[0])
            input_list.remove(input_list[0])


    return op_list





#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):
    input.sort()
    return input

    #return sorted(input)

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    found=False
    for element in input:
        if element==value:
            found=True
    return found



#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    return value in input

if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]


    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
