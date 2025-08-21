import itertools

def optimized_brute_force(items, capacity):
    """0/1 Knapsack problem with brute force and early termination"""
    n = len(items)
    best_value = 0
    best_combination = None
    
    for i in range(1, 2**n):
        total_weight = 0
        total_value = 0
        
        # Convert to binary representation
        binary = format(i, f'0{n}b')
        
        for j in range(n):
            if binary[j] == '1':
                weight, value = items[j]
                total_weight += weight
                total_value += value
                
                # Early termination if overweight
                if total_weight > capacity:
                    break
        
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combination = binary
    
    return best_combination, best_value

# Example
items = [(2, 10), (3, 15), (5, 25), (7, 40)]  # (weight, value)
capacity = 10
combination, value = optimized_brute_force(items, capacity)
print(f"Best combination: {combination}, Total value: {value}")