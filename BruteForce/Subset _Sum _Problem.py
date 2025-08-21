import itertools

def subset_sum_brute_force(numbers, target):
    """Find if any subset sums to target using brute force"""
    for r in range(1, len(numbers) + 1):
        for subset in itertools.combinations(numbers, r):
            if sum(subset) == target:
                return subset
    return None

# Example
numbers = [3, 34, 4, 12, 5, 2]
target = 9
result = subset_sum_brute_force(numbers, target)
print(f"Subset that sums to {target}: {result}")