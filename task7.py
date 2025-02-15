import random
from collections import defaultdict

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_dice_rolls(num_simulations):
    results = defaultdict(int)
    
    for _ in range(num_simulations):
        total = roll_dice()
        results[total] += 1
    
    probabilities = {sum_value: (count / num_simulations) * 100 
                    for sum_value, count in results.items()}
    
    return probabilities


num_simulations = 1000000
    
probabilities = simulate_dice_rolls(num_simulations)
    
print("Сума | Імовірність")
for sum_value in range(2, 13):
    probability = probabilities.get(sum_value, 0)
    print(f"{sum_value:4d} | {probability:6.2f}%")