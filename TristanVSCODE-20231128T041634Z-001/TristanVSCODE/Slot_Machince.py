#Tristan Perez
#1/25/24
#Slot Machine
#Initialize
import random

credit = 100 
#Funcations
slot = [ '♥', '♦', '♠', '♣', '☆', '7']
print("----------------------- Welcome to slot machine -----------------------")
print("Slot machine Symbols: ['♥', '♦', '♠', '♣', '☆', '7'] ")
print("you have 100 credits. Each spin costs 10 credits.")

def SpinSlots():
    global credit
    roll = None
    spin_slot = input("Do you want to spin a slot? (y/n)")
    if spin_slot.lower() == 'y' or spin_slot.lower() == 'yes':
        credit -= 10
        roll = (random.choice(slot),random.choice(slot),random.choice(slot))
        print("Current Slots: " + ' '.join(map(str, roll))) 
        print("current credits: "+ str(credit))
    if roll == ('♥', '♥', '♥') or roll == ('♦', '♦', '♦') or roll == ('♠', '♠', '♠') or roll == ('♣', '♣', '♣') or roll == ('☆', '☆', '☆'):    
        print("Congratulations, you got a match")
        credit += 50
    if roll == ('7', '7', '7'):
        print("jackpot")
        credit += 500
    

# def playagain():
#     play = input("Do you want to play again? (y/n)")
#     if play.lower() == 'y' or play.lower() == 'yes':


#     if spin_slot.lower() in ['y', 'n', 'yes', 'no']:
#     # proceed with your code
# else:
#     print("Please enter a valid response (y/n or yes/no)")


#Main
