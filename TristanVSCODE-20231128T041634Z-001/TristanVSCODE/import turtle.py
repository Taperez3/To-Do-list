#tristan perez
#APCSP
#int
#functions 
import turtle
def get_user_input():
    name = turtle.textinput("Ticket Sales Form", "Enter your name:")
    age = int(turtle.textinput("Ticket Sales Form", "Enter your age:"))
    day = turtle.textinput("Ticket Sales Form", "Enter the day of the week:").lower()
    coupon_code = turtle.textinput("Ticket Sales Form", "Enter the coupon code (if any):").upper()
    return name, age, day, coupon_code

def calculate_ticket_price(age, day, coupon_code):
    if age <= 3:
        return 0
    elif age <= 18:
        if day == 'friday' and coupon_code == 'FREEFRIDAY':
            return 0
        elif day == 'sunday' and coupon_code == 'SUNDAY10':
            return 10
        return 0.5 if day in ['monday', 'tuesday', 'wednesday', 'thursday'] else 1
    else:
        return 1

def display_ticket_info(name, day, price):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 50)
    turtle.write("Ticket Information", move=False, align='center', font=('Arial', 16, 'normal'))
    turtle.goto(0, 20)
    ticket_info = "Name: " + name + "\nDay: " + day + "\nPrice: $" + format(price, ".2f")
    turtle.write(ticket_info, move=False, align='center', font=('Arial', 12, 'normal'))
    turtle.done()

def main():
    name, age, day, coupon_code = get_user_input()
    price = calculate_ticket_price(age, day, coupon_code)
    display_ticket_info(name, day, price)

# Call the main function
main()
