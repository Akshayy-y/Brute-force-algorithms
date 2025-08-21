def brute_force_string_search(text, pattern):
    """Brute force string pattern matching"""
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i  # Pattern found at index i
    
    return -1  # Pattern not found

# Example
text = "ABABDABACDABABCABAB"
pattern = "ABABC"
position = brute_force_string_search(text, pattern)
print(f"Pattern found at position: {position}")