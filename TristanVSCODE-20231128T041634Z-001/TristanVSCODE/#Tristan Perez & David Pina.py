#Tristan Perez & David Pina
#Root Beer
#11/27/23

def bottlesRB(): #This function repeats the lines of the song while subtracting each time until it reaches the end of the song 
    x = 99
    for i in range(98):
        print(str(x) + " bottles of root beer on the wall " + str(x) + " bottles of root beer " )
        x = x - 1
        print (" Take one down and pass it around " + str(x) + " bottles of root beer on the wall ")

    print(str(x) + " bottle of root beer on the wall " + str(x) + " bottle of root beer on the wall ")
    x = x - 1
    print(" Take one down and pass it around " + str(x) + " bottles of root beer on the wall ")
    print(" no more bottles of root beer on the wall ")
    print(" Go to the store and buy some more, 99 bottles of beer on the wal. ")


bottlesRB()
