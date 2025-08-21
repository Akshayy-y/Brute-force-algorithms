import itertools
import string
import threading
import time

class BruteForceThread(threading.Thread):
    def __init__(self, chars, length, start_char, end_char, target):
        threading.Thread.__init__(self)
        self.chars = chars
        self.length = length
        self.start_char = start_char
        self.end_char = end_char
        self.target = target
        self.found = None
    
    def run(self):
        # Generate only a portion of the search space
        for guess in itertools.product(self.chars, repeat=self.length):
            current = ''.join(guess)
            if current[0] < self.start_char or current[0] > self.end_char:
                continue
            if current == self.target:
                self.found = current
                return

def parallel_brute_force(target, num_threads=4):
    """Multi-threaded brute force attack"""
    chars = string.ascii_lowercase
    length = len(target)
    threads = []
    
    # Split search space by first character
    chunk_size = len(chars) // num_threads
    
    for i in range(num_threads):
        start_char = chars[i * chunk_size]
        end_char = chars[(i + 1) * chunk_size - 1] if i < num_threads - 1 else chars[-1]
        
        thread = BruteForceThread(chars, length, start_char, end_char, target)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
        if thread.found:
            return thread.found
    
    return None

# Example (use with caution - for demonstration only)
result = parallel_brute_force("test", 4)
print(f"Found: {result}")