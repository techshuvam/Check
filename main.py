
from itertools import permutations
from math import factorial

# Input
word = input("Enter a word: ")

# Generate all unique arrangements
ways = sorted(set(permutations(word)))

# Convert tuples into strings
ways = [''.join(p) for p in ways]

# Output 1: All possible arrangements
print("\n1. All possible ways:")
print(", ".join(ways))

# Output 2: Total number of unique arrangements
print("\n2. Total count:", len(ways))
