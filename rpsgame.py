print("---------------------------")
print("  Rock Paper Scissors v1")
print("---------------------------")

player_1 = input("Enter player 1's name: ")
player_2 = input("Enter player 2's name: ")

rolls = ['rock', 'paper', 'scissors']

roll1 = input(f"{player_1}, what is your roll? [rock, paper, scissors]:")
roll2 = input(f"{player_2}, what is your roll? [rock, paper, scissors]:")

print(f"{player_1} rolls {roll1}")
print(f"{player_2} rolls {roll2}")

# Test for a winner
# Rock
#     Rock -> tie
#     Paper -> lose
#     Scissors -> win
# Paper 
#     Rock -> win 
#     Paper -> tie 
#     Scissors -> lose
# Scissors 
#     Rock -> lose 
#     Paper -> win 
#     Scissors -> tie 

