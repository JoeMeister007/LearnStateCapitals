import capital_info
import random

def multiple_choice():
    print()
    print("Multiple Choice")
    print("Type the NUMBER of the correct answer")
    print("Type q to quit")

    while True:
        #pick random states
        random_states = random.sample(capital_info.states, k=3)
        state = random_states[0] #the first is ours
        #add the correct capital to our list of cities
        cities = [state["capital"]]
        #add a decoy from the same state
        cities.append(random.choice(state["other_cities"]))
        #add capitals from two other states
        for i in range(1,len(random_states)):
            cities.append(random_states[i]["capital"])

        #shuffle it up
        random.shuffle(cities)

        #ready to roll
        print()
        print(state["name"])
        for i in range(len(cities)):
            print(str(i + 1) + " - " + cities[i])
        guess = input("Capital: ")
        guess = guess.strip()
        if guess == "q":
            break
        try:
            idx = int(guess)
            if cities[idx - 1] == state["capital"]:
                print("Correct!")
            else:
                print("Incorrect. It's " + state["capital"])
        except:
            print("Incorrect. It's " + state["capital"])
        
        

def short_answer():
    print()
    print("Short Answer")
    print("Type out the correct capital")
    print("Type q to quit")

    while True:
        #pick random states
        state = random.choice(capital_info.states)

        #ready to roll
        print()
        print(state["name"])
        guess = input("Capital: ")
        guess = guess.strip()
        if guess == "q":
            break
        elif guess.lower() == state["capital"].lower():
            print("Correct!")
        else:
            print("Incorrect. It's " + state["capital"])

print("""Welcome! This program helps you memorize the state captials.
It will give you a state and you must list the capital.""")

while True:
    print("""Please select one of the following options:
1 - Multiple Choice
2 - Short Answer
q - Quit""")
    option = input()
    option = option.strip()
    if option == "1":
        multiple_choice()
    elif option == "2":
        short_answer()
    elif option == "q":
        break
    else:
        print("Invalid Input")
