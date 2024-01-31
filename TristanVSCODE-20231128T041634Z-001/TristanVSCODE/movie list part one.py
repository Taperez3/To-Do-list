#Name: Tristan Perez, Ricardo Fonseca
#1/10
#AP CSP

#Initialize
myList = ["Indiana Jones", "Star Wars", "Ted", "Superman", "Superbad", "The Joker"]
print("Welcome to To-Do List!")
print("Please choose an operation ny entering a number 1-5")
print("1 = Add a task \n2 = View current movie list \n3 = Mark movie as completed \n4 = Remove a move from the to-do list \n5 = Quit")
option = int(input("Option: "))

def add():
    global x
    x = int(input("Where would you like to place new task? #Select a number 0-5: "))
    myList.insert(x, "Up")
    print(myList)

def view():
    print(myList)

def mark():
    myList = ["Indiana Jones", "Star Wars", "Ted", "Superman", "Superbad", "The Joker"]
    ans = input("Which movie would you like to as complete?: ")
    index = myList.index(ans)
    print("completed")

def remove():
    removal = int(input("Which movie would you like to remove? 0 is first movie on the list and last movie is 5: "))
    myList.pop(removal)
    print(myList)


def run():
    
    if option == 1: 
        add()

    if option == 2:
        view()

    if option == 3:
        mark()

    if option == 4:
        remove()
    
    if option == 5:
        quit()

        
#main
run()