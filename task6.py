def greedy_algorithm(items, budget):
    efficiency = {
        item: items[item]["calories"] / items[item]["cost"]
        for item in items
    }
    
    sorted_items = sorted(efficiency.items(), key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, _ in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    selected = [[set() for _ in range(budget + 1)] for _ in range(n + 1)]
    
    items_list = list(items.items())
    
    for i in range(1, n + 1):
        item_name, item_data = items_list[i-1]
        cost = item_data["cost"]
        calories = item_data["calories"]
        
        for w in range(budget + 1):
            if cost <= w:
                if dp[i-1][w] < dp[i-1][w-cost] + calories:
                    dp[i][w] = dp[i-1][w-cost] + calories
                    selected[i][w] = selected[i-1][w-cost] | {item_name}
                else:
                    dp[i][w] = dp[i-1][w]
                    selected[i][w] = selected[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]
                selected[i][w] = selected[i-1][w]
    
    selected_items = list(selected[n][budget])
    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in selected_items)
    
    return selected_items, total_calories, total_cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
print(f"!!! Greedy (budget = {budget}):")
print(f"Selected items: {greedy_items}")
print(f"Total calories: {greedy_calories}")
print(f"Total cost: {greedy_cost}")
    

dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
print(f"!!! Dynamic Programming (budget = {budget}):")
print(f"Selected items: {dp_items}")
print(f"Total calories: {dp_calories}")
print(f"Total cost: {dp_cost}")