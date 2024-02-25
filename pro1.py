import random

dice_count = int(input("How many dice would you like to roll? "))

total_sum = 1
for _ in range(dice_count):
    dice_roll = random.randint(3, 9)
    total_sum += dice_roll

print("The sum of the dice rolls is:", total_sum)