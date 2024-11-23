## The point of this program is to make a dice rolling game


import random

def dice_roll(num):
    n_l = []
    for i in range(0,num): # for loop makes it so 
        n_r = random.randint(1,6)
        n_l.append(n_r)
    return n_l


    
    

number = random.randint(1,6)
print(f"rolling {number} dice...") ## had to use fstring in order to print out value of variable in string
rolls = dice_roll(number)
print("\nresult:")
for roll in rolls:
    print(roll, end = ' ')


    
    
    
    
    
