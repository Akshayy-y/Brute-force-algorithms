import itertools
import math

def tsp_brute_force(points):
    """Solve TSP using brute force (only for small n)"""
    n = len(points)
    if n <= 1:
        return points, 0
    
    min_distance = float('inf')
    best_path = None
    
    # Generate all permutations of points
    for path in itertools.permutations(range(1, n)):
        current_path = [0] + list(path)  # Start from point 0
        total_distance = 0
        
        # Calculate total distance
        for i in range(len(current_path) - 1):
            p1 = points[current_path[i]]
            p2 = points[current_path[i + 1]]
            total_distance += math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        
        # Add return to start
        p1 = points[current_path[-1]]
        p2 = points[current_path[0]]
        total_distance += math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = current_path
    
    return best_path, min_distance

# Example
points = [(0, 0), (1, 2), (3, 1), (2, 3)]
path, distance = tsp_brute_force(points)
print(f"Best path: {path}, Distance: {distance:.2f}")