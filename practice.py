import capital_info
import random

def multiple_choice():
    print()
    print("Multiple Choice")
    print("Type the NUMBER of the correct answer")
    print("Type q to quit")

    #get all the states in a random order
    state_queue = []
    correct_list = []
    incorrect_list = []

    correct_redo_prob = 0.05 #the probability of getting a previous correct question
    incorrect_redo_prob = 0.20 #the probability of getting a previous incorrect question
    while True:
        #if we've gone through all the states reset
        if len(state_queue) == 0 :
            state_queue = capital_info.states.copy()
            random.shuffle(state_queue)

            correct_list = []
            incorrect_list = []
        redo_rand = random.random()

        #there's a probability that we redo an answer we got correct
        if redo_rand < correct_redo_prob:
            if len(correct_list) > 0:
                state_queue.insert(0, correct_list.pop(0))
        #that didn't happen
        else:
            redo_rand -= correct_redo_prob
            #there's a probability that we redo an answer we got wrong
            if redo_rand < incorrect_redo_prob:
                if len(incorrect_list) > 0:
                    state_queue.insert(0, incorrect_list.pop(0))

        #get our state from the front of the queue
        state = state_queue.pop(0)
        #add the correct capital to our list of cities
        cities = [state["capital"]]
        #add a decoy from the same state
        cities.append(random.choice(state["other_cities"]))
        
        
        #pick some other random states (3 cause one might be ours)
        random_states = random.sample(capital_info.states, k=3)

        #add capitals from two other states
        for i in range(0,len(random_states)):
            if random_states[i]["name"] ==state["name"]:
                continue

            cities.append(random_states[i]["capital"])
            if len(cities) >= 4:
                break

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
                correct_list.append(state)
            else:
                print("Incorrect. It's " + state["capital"])
                incorrect_list.append(state)
        except:
            print("Incorrect. It's " + state["capital"])
        
        

def short_answer():
    print()
    print("Short Answer")
    print("Type out the correct capital")
    print("Type q to quit")

    #get all the states in a random order
    state_queue = []
    correct_list = []
    incorrect_list = []

    correct_redo_prob = 0.05 #the probability of getting a previous correct question
    incorrect_redo_prob = 0.20 #the probability of getting a previous incorrect question
    while True:
        #if we've gone through all the states reset
        if len(state_queue) == 0 :
            state_queue = capital_info.states.copy()
            random.shuffle(state_queue)

            correct_list = []
            incorrect_list = []
        redo_rand = random.random()

        #there's a probability that we redo an answer we got correct
        if redo_rand < correct_redo_prob:
            if len(correct_list) > 0:
                state_queue.insert(0, correct_list.pop(0))
        #that didn't happen
        else:
            redo_rand -= correct_redo_prob
            #there's a probability that we redo an answer we got wrong
            if redo_rand < incorrect_redo_prob:
                if len(incorrect_list) > 0:
                    state_queue.insert(0, incorrect_list.pop(0))

        #get our state from the front of the queue
        state = state_queue.pop(0)

        #ready to roll
        print()
        print(state["name"])
        guess = input("Capital: ")
        guess = guess.strip()
        if guess == "q":
            break
        elif guess.lower() == state["capital"].lower():
            print("Correct!")
            correct_list.append(state)
        else:
            print("Incorrect. It's " + state["capital"])
            incorrect_list.append(state)

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
