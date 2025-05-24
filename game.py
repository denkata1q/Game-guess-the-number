import random
comp_num=random.randint(1,100)
while True:
    player_input=input("Guess the number (1-100): ")
    if player_input.isdigit():
        number=int(player_input)
        if number > comp_num:
            print("To High")
            continue
        elif number<comp_num:
            print("To Low")
            continue
        elif number==comp_num:
            print("You guess it")
            break

    elif not player_input.isdigit():
        print("Invalid input! Try again...")
        continue

