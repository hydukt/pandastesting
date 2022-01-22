from sys import exit
from sys import argv
import time

game, name = argv


#gameshow room - first on right
def gameshow_room(pathtaken):
    
    current_points = 0
    points_needed = 10

    question1 = "What's your name?"
    answer1 = name

    question2 = "7*3 = ?"
    answer2 = 7*3

    question3 = "What direction did you take at the start?"
    answer3 = pathtaken

    question4 = "What's the first word in this sentence alphabetically"
    answer4 = question4.lower()
    answer4 = answer4.split(' ')
    answer4 = sorted(answer4)

    print(answer4)


    print("Now you must answer a few questions. Correct answers are worth four points, wrong answers lose you one point. You must reach 10 points to pass.")

    time.sleep(1)

    print(f"\n {question1}")

    time.sleep(1)

    submitted1 = input("> ")

    time.sleep(1)

    if submitted1.lower() == answer1.lower():
        current_points += 4
        print(f"\n{submitted1} is correct. You gain 4 points. You now have {str(current_points)} points.")
    else:
        current_points -= 1
        print(f"\n{submitted1} is incorrect. The correct answer was {answer1}. You now have {str(current_points)} points.")

    time.sleep(1)

    print(f"\n {question2}")

    time.sleep(1)

    submitted2 = input("> ")

    time.sleep(1)

    if submitted2.lower() == str(answer2).lower():
        current_points += 4
        print(f"\n{submitted2} is correct. You gain 4 points. You now have {str(current_points)} points.")
    else:
        current_points -= 1
        print(f"\n{submitted2} is incorrect. The correct answer was {answer2}. You now have {str(current_points)} points.")

    time.sleep(1)
    
    print(f"\n {question3}")

    time.sleep(1)

    submitted3 = input("> ")

    time.sleep(1)

    if submitted3.lower() == str(answer3).lower():
        current_points += 4
        print(f"\n{submitted3} is correct. You gain 4 points. You now have {str(current_points)} points.")
    else:
        current_points -= 1
        print(f"\n{submitted3} is incorrect. The correct answer was {answer3}. You now have {str(current_points)} points.")

    time.sleep(1)
    
    print(f"\n {question4}?")

    time.sleep(1)

    submitted4 = input("> ")

    time.sleep(1)

    if submitted4.lower() ==  answer4[0].lower():
        current_points += 4
        print(f"\n{submitted4} is correct. You gain 4 points. You now have {str(current_points)} points.")
    else:
        current_points -= 1
        print(f"\n{submitted4} is incorrect. The correct answer was {answer4[0]}. You now have {str(current_points)} points.")
    


#words room - last on left
def words_room():
    
    print(f"Please enter a sentence of at least 5 words.")

    sentence = input("> ")
    words = sentence.split(' ')

    if len(words) > 4:
        words = sorted(words)
    else:
        dead("I said at least 5 words")

    print(f"What was the first word, alphabetically, of the sentence you provided?")

    first_word = input("> ")

    if first_word.lower() == words[0].lower():
        print(f"Good, now the last word?")
        last_word = input("> ")
        
        if last_word.lower() == words[-1].lower():
            print(f"Good job.")
        else:
            dead("You don't know your alphabet very well.")
    else:
        dead("You don't know your alphabet very well.")

#rpg room - seconds on left
def turn_based():
    enemy_name = ""

    for i in range(len(name)):
        enemy_name = enemy_name + name[-i-1]

    print(f"Now {name}, you face off against the evil {str.title(enemy_name)}")

    boss_health = 40
    player_health = 40

    physical_damage = 5
    ice_damage = 10
    fire_damage = -1

    boss_damage = 8

    while boss_health > 0:

        time.sleep(2)

        print(f"""\n\n{str.title(enemy_name)} looks at you with fiery eyes, what will you do?
            1) Attack with fists.
            2) Attack with fire.
            3) Attack with ice.""")
        
        inputchoicevalid = False

        while inputchoicevalid == False:
            choice = input(">  ")
            try:
                choicecheck = int(choice)
                inputchoicevalid = True
            except ValueError as e:
                print("Not a valid choice, enter something else")



        if int(choice) == 1:
            print(f"\n\nYou punch {str.title(enemy_name)}, dealing 5 damage")
            boss_health = boss_health - 5

            if boss_health > 0:
                print(f"\n{str.title(enemy_name)} strikes you for 8 damage")
                player_health = player_health - 8

            time.sleep(1)

            print(f"\n\n{name} health remaining: {player_health} \n{str.title(enemy_name)} health remaining: {boss_health}")

            time.sleep(1)
        
        elif int(choice) == 2:
            print(f"\n\nYou throw a fireball at {str.title(enemy_name)}. He resists, gains 1 health")
            boss_health = boss_health + 1

            if boss_health > 0:
                print(f"\n{str.title(enemy_name)} strikes you for 8 damage")
                player_health = player_health - 8

            time.sleep(1)

            print(f"\n\n{name} health remaining: {player_health} \n{str.title(enemy_name)} health remaining: {boss_health}")

            time.sleep(1)

        elif int(choice) == 3:
            print(f"\n\nYou throw an ice shard at {str.title(enemy_name)}. It's super effective, dealing 10 damage")
            boss_health = boss_health - 10

            if boss_health > 0:
                print(f"\n{str.title(enemy_name)} strikes you for 8 damage")
                player_health = player_health - 8

            time.sleep(1)

            print(f"\n\n{name} health remaining: {player_health} \n{str.title(enemy_name)} health remaining: {boss_health}")

            time.sleep(1)
        
        else:
            print(f"\n\nInvalid Choice")
        
        if player_health < 1:
            dead(f"\n\nYou were killed by {str.title(enemy_name)}")

        if boss_health < 1:
            print(f"\n\nYou've defeated {str.title(enemy_name)}, proceed to the final room")


    #math room - first room on the left
def math_room():

    question_types = ["addition", "subtraction", "multiplication", "division"]

    print("This room is a math test.")
    print("Which type of question do you want?")

    for i in range(len(question_types)):
        print(f"\n {i+1}. {question_types[i]}")

    choice = input("1/2/3/4?   ")

    if int(choice) == 1:
        answer = input("3+17 = ?   ")
        if int(answer) == 3+17:
            print("That was easy. Proceed to the next room")
        else:
            dead("Dumbass")
    elif int(choice) == 2:
        answer = input("20-13 = ?   ")
        if int(answer) == 20-13:
            print("Lucky guess. Proceed to the next room")
        else:
            dead("Idiot")
    elif int(choice) == 3:
        answer = input("40*4 = ?   ")
        if int(answer) == 40*4:
            print("Good job. You may proceed")
        else:
            dead("Wrong")
    elif int(choice) == 4:
        answer = input("100/5 = ?   ")
        if int(answer) == 100/5:
            print("Fine...go ahead.")
        else:
            dead("Nope")
    else:
        dead("How do you expect to do math if you can't even get the number right.")

    
#start room
def start():
    print(f"Welcome to the game {name}.")
    print("You will face a series of challenges, your choices determine your success.")
    print("Which way will you go?")

    while True:
        choice = input("Left/Right?:    ")
        if choice == "left":
            math_room()
        elif choice == "right":
            right_room2()
        else:
            print("Invalid choice")

#all roads end here
def dead(reason):
    print(reason, "You die now!")

    print(f"Do you want to play again, {name}")
    
    play_again = input("Y, N: ").upper()

    if play_again == "Y":
        words_room()
    elif play_again == "N":
        exit(0)
    else:
        print("You still don't get it, do you?")
        exit(0)

gameshow_room("left")



#one room earn gold
#one room spend gold

