import random

def roll_dice(dice_type):
    return random.randint(1, dice_type)

# Бросок кубика d20
d20_roll = roll_dice(20)