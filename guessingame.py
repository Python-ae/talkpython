import random


print("-------------------------------")
print("     M&M guessing game!")
print("-------------------------------")



mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How many MMs are in the jars? ")
    guess = int(guess_text)
    attempts += 1

    if  mm_count == guess:
        print(f"You got a free lunch! It was {guess}")
        break
    elif guess < mm_count:
        print("Sorry, that's too LOW")
    else:
        print("That's too HIGH!")

print(f"Bye, you're done in {attempts}!")

# print(mm_count)


