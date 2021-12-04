
#class elevationChange:
    #f = open('inputDayOne.txt','r')
    #elevationList = f.readlines()
    #f.close()

def checkIncreaseElevation(elevationList):
    count = 0
    n = len(elevationList)
    for i in range(0, n - 1):
        if elevationList[i]< elevationList[i+1]:
            count = count +1
    return count

def castInputToInts(elevationList):
    fixedList = []
    for i in range(0, len(elevationList)):
       fixedList.append(int(elevationList[i])) 

    return fixedList

def checkIncreaseElevationAvg3(elevationList):
    count = 0
    n = len(elevationList)
    for i in range(0, n - 3):
        curr = elevationList[i] + elevationList[i+1] + elevationList[i+2]
        next = elevationList[i+1] + elevationList[i+2] + elevationList[i+3]
        if curr < next:
            count = count +1
    return count


def main():
    f = open('inputDayOne.txt','r')
    elevationList = castInputToInts(f.readlines())
    f.close()
    print(checkIncreaseElevation(elevationList))
    print(checkIncreaseElevationAvg3(elevationList))


if __name__ == '__main__':
    main()