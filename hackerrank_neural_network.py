#!/usr/bin/env python3
"""
HackerRank Problem: Neural Network Generations

A neural network has n layers. In each generation:
- Odd generations: 1 neuron can be added to at most one layer
- Even generations: 2 neurons can be added to at most one layer

Find the minimum generation in which all layers can have an equal number of neurons.

Example:
n = 4
layer = [1, 1, 2, 4]

Generation 1 (odd): add 1 to layer[0] -> [2, 1, 2, 4]
Generation 2 (even): add 2 to layer[0] -> [4, 1, 2, 4]
Generation 3 (odd): add 1 to layer[1] -> [4, 2, 2, 4]
Generation 4 (even): add 2 to layer[1] -> [4, 4, 2, 4]
Generation 5: skip
Generation 6 (even): add 2 to layer[2] -> [4, 4, 4, 4]

Answer: 6
"""

def simulate_generations(deficits):
    """Find minimum generations using BFS."""
    from collections import deque

    if all(d == 0 for d in deficits):
        return 0

    # BFS: (deficits_state, generation)
    # visited tracks (state, generation_parity) to allow revisiting at different parities
    queue = deque([(tuple(deficits), 0)])
    visited = {(tuple(deficits), 0)}

    while queue:
        state, gen = queue.popleft()

        # Try next generation
        next_gen = gen + 1
        capacity = 1 if next_gen % 2 == 1 else 2
        next_parity = next_gen % 2

        # Collect all possible next states
        candidates = []

        # Option 1: Skip this generation
        candidates.append(state)

        # Option 2: Work on each layer that can use this generation
        for i, deficit in enumerate(state):
            if deficit >= capacity:
                new_state = list(state)
                new_state[i] -= capacity
                candidates.append(tuple(new_state))

        # Add unvisited (state, parity) combinations to queue
        for next_state in candidates:
            # Check if done
            if all(d == 0 for d in next_state):
                return next_gen

            key = (next_state, next_parity)
            if key not in visited:
                visited.add(key)
                queue.append((next_state, next_gen))

    return float('inf')  # Should never reach here


def greedy_simulate(deficits):
    """Greedy simulation as fallback for large inputs."""
    deficits = list(deficits)
    generation = 0

    while any(d > 0 for d in deficits):
        generation += 1
        capacity = 1 if generation % 2 == 1 else 2

        best_idx = -1
        # Prefer matching parity
        for i, deficit in enumerate(deficits):
            if deficit >= capacity and deficit % 2 == capacity % 2:
                best_idx = i
                break

        # Otherwise use any
        if best_idx == -1:
            for i, deficit in enumerate(deficits):
                if deficit >= capacity:
                    best_idx = i
                    break

        if best_idx != -1:
            deficits[best_idx] -= capacity

    return generation


def findMinGeneration(layer):
    """
    Find the minimum generation in which all layers can have equal neurons.

    Key insight: Try different target values and pick the one that minimizes
    the generation count. Higher targets may be faster due to better use of
    even generations (which add 2 neurons).

    Args:
        layer: list of integers representing neurons in each layer

    Returns:
        long: minimum number of generations needed
    """
    if not layer:
        return 0

    max_val = max(layer)

    # Try different targets starting from max_val
    min_generations = float('inf')

    # Check targets from max_val up to a reasonable upper bound
    # Pattern: higher targets eventually become worse, so we can stop early
    for target in range(max_val, max_val + 1000):
        deficits = [target - x for x in layer]

        if any(d < 0 for d in deficits):
            continue

        generations = simulate_generations(deficits)
        min_generations = min(min_generations, generations)

        # Early termination: if we're getting worse for several iterations
        if generations > min_generations + 20:
            break

    return min_generations


if __name__ == '__main__':
    # Read input
    n = int(input().strip())
    layer = []
    for _ in range(n):
        layer.append(int(input().strip()))

    # Calculate and print result
    result = findMinGeneration(layer)
    print(result)
