#!/usr/bin/env python3
from hackerrank_neural_network import simulate_generations

# Test case: [1,1,2,4] with target 4
print("\n[1,1,2,4] -> target 4, deficits [3,3,2,0]")
result = simulate_generations([3,3,2,0])
print(f"Result: {result} generations")

# Test case: [1,1,1,1,2] with different targets
print("\n[1,1,1,1,2] -> target 2, deficits [1,1,1,1,0]")
result = simulate_generations([1,1,1,1,0])
print(f"Result: {result} generations")

print("\n[1,1,1,1,2] -> target 3, deficits [2,2,2,2,1]")
result = simulate_generations([2,2,2,2,1])
print(f"Result: {result} generations")
