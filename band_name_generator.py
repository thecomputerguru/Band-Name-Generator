from random import choice   #Import random.choice
    
def select_answer():
    global first_string, second_string   #Set "first_string" and "second_string" as global variables for use in "main" function
    first_string = choice(answers)   #Have computer select an answer
    second_string = choice(answers)   #Have computer select an answer
    if first_string == second_string:   #Check if the computer picked the same answer for the "first_string" variable and the "second_string" variable
        select_answer()   #If computer selected the same answer for both string variables, select another answer
    else:
        pass   #If computer selected two different answers, then continue

def main():
    global answers   #Set "answer" variable to global for use in "select_answer" function
    answers = []   #Create list where answers will be stored
    print("Band name generator")
    print("")
    city_born_in = input("What city were you born in? ")   #Ask questions
    favorite_color = input("What is your favorite color? ")
    favorite_drink = input("What is your favorite drink? ")
    favorite_animal = input("What is your favorite animal? ")
    answers.append(city_born_in)   #Add answers to "answers" list
    answers.append(favorite_color)
    answers.append(favorite_drink)
    answers.append(favorite_animal)
    select_answer()   #Computer selects answers
    print("Generated band name: "+first_string+" "+second_string)
    
main()
    
    


