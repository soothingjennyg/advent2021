from os import X_OK

def main():
    x = 0
    z = 0
    aim = 0

    f = open('inputDayTwo.txt','r')
    commandList = f.readlines()

    for item in commandList:
        data = item.split()
        cmd = data[0]
        val = data[1]
        if (cmd == 'forward'):
            x = x + int(val)
            z = z + int(val) * aim
        elif (cmd == 'up'):
            #z = z - int(val)
            aim = aim - int(val)   
        elif (cmd == 'down'):
            #z = z + int(val)
            aim = aim + int(val)   

    print( x )
    print( z )
    print( x * z )

if __name__ == '__main__':
    main()