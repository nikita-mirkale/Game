import random

# Dictionary to map the user's choice
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the computer's random choice
computer = random.choice([1, -1, 0])  # Randomly chooses between Snake, Water, Gun

# Get user input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Check if the user's input is valid
if youstr not in youDict:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    you = youDict[youstr]  

    # Display choices
    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    # Logic to determine the winner
    if computer == you:
        print("It's a draw!")
    else:
        # Winning and losing conditions
        if (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
            print("You win!")
        else:
            print("You lose!")