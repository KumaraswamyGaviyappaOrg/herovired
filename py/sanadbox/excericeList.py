myList = [] 
myset = {}
myTuple = ()

def switch(var):
    if var == 1:
        val = input("Enter the value: ")
        updateList(val)
    elif var == 2:
        val = input("Enter the value: ")
        updateSet(val)
    elif var == 3:
        val = input("Enter the value: ")
        updateTuple(val)
    else:
        return False    
    
def updateList(var):
    myList.append(var)
    print(myList)
def updateSet(var):
    myset.add(var)
    print(myset)
def updateTuple(var):
    myTuple += (var,)
    print(myTuple)

def ListOperations(myList):
    print("Current List : ", myList)
    while True:
        print("Current List : ", myList)
        val = input("Enter 1:add List 2:remove List 3:clear List 4:exit: ")

        if int(val) == 1:
            val = input("Enter the value: ")
            myList.append(val)
        elif int(val) == 2:
            val = input("Enter the value: ")
            myList.remove(val)
        elif int(val) == 3:
            myList.clear()
        else:
            print("Update List : " , myList)
            print("Exiting...")
            return

def tupleOperations(myTuple):
    print("Current List : ", myTuple)
    while True:
        val = input("Enter 1:add List 2:remove List 3:clear List 4:exit: ")

        if int(val) == 1:
            val = input("Enter the value: ")
            myTuple.append(val)
        elif int(val) == 2:
            val = input("Enter the value: ")
            myTuple.remove(val)
        elif int(val) == 3:
            myTuple.clear()
        else:
            print("Update List : " , myTuple)
            print("Exiting...")
            break
def main():

    ListOperations(myList)
        # val = input("Enter 1: ListOperations 2: updateset 3: updatetuple: 4:exit: ")
        # switch(int(val))
        # if int(val) == 4:
        #     print("Exiting...")
        #     break

main()











