import random 

rooms = ['living room', 'kitchen', 'bedroom', 'drawing room']

treasure = random.choice(rooms)

location = input(f"Please start the game by selecting any one location from the given locations in house: ")


while True:
    if treasure != location:
        print("Treasure not here")
        input("Please try again: ")
    else:
        print("Treasure found")
        break
