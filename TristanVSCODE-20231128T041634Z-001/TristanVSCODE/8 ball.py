#Name:Tristan.p 
#Date:1/19/24
#8 Ball Program
import random

def magic_8_ball():
    responses = ["Yes definitely","No, not at all.","maybe i don't know","ask me later","of course","yesss sirr","Don't count on it","Without a doubt","yes", "no"]

    while True:
        user_question = input("Ask the Magic 8 Ball a yes-or-no question: ")

        if not user_question.endswith('?'):
            print("Please enter a valid question ending with a question mark.")
            continue

        chosen_response = random.choice(responses)
        print("Magic 8 Ball says: " + chosen_response)
        
        another_question = input("Do you want to ask another question? (yes/no): ")
        if another_question != 'yes' and another_question != 'y':
            print("Exiting the 8 Ball Program, have a good day")
            break


#main 
magic_8_ball()
