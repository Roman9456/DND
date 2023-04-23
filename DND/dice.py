import random

# функция для броска кубика
def roll_dice(number_of_dice, sides_of_dice):
    result = 0
    for i in range(number_of_dice):
        result += random.randint(1, sides_of_dice)
    return result
# бросок 2d6
print(roll_dice(2, 6))

# бросок d20
print(roll_dice(1, 20))