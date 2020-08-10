import time
import random

str1 = ["As-salamu alaykum", "Salam Alaykum", "Hala", "WooooooooooooW"]

for i in range(1,101):
    # print("{}. {}".format(str(i).zfill(2), str1))
    randomNum = random.randint(2, 50)
    # if randomNum == 10 or randomNum == 20 or randomNum == 30 or randomNum == 50:
    if randomNum in [10, 20, 30, 40, 50]:
        print(f"Sleeping IF ---------{randomNum}---------- Sleeping IF")
        time.sleep(2)
        continue
    print(f"{str(i).zfill(randomNum)}. {random.choice(str1)}")
    time.sleep(0.1)
print("---------The End----------")