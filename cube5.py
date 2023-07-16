import random

def roll_dice():
  
    dice1 = random.randint(5, 6)
    dice2 = random.randint(5, 6)
    
    # Check if both dice show one
    if dice1 == 5 and dice2 == 5:
        return True
    else:
        return False


count = 0

while True:
    user_input = input("Enter 'r' to roll the dice or 'q' to quit: ")
    
    if user_input == 'r':
        if roll_dice():
            count += 1
            print("Two ones occurred!")
        else:
            print("No two ones.")
    elif user_input == 'q':
        break
    else:
        print("Invalid input. Try again.")

print(f"The number of times two ones occurred: {count}")
