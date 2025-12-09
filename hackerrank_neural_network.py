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

def findMinGeneration(layer):
    """
    Find the minimum generation in which all layers can have equal neurons.

    Args:
        layer: list of integers representing neurons in each layer

    Returns:
        long: minimum number of generations needed
    """
    if not layer:
        return 0

    # Target is the maximum value (we can only add neurons, not remove)
    target = max(layer)

    # Calculate deficit for each layer
    deficits = [target - x for x in layer]

    # Process each deficit sequentially
    # Key insight: stick with one layer and use odd+even pairs efficiently
    # Pattern: odd gen adds 1, even gen adds 2
    generation = 0

    for deficit in deficits:
        remaining = deficit

        # Process this layer's deficit completely before moving to next
        while remaining > 0:
            generation += 1

            if generation % 2 == 1:  # Odd generation: add 1 neuron
                remaining -= 1
            else:  # Even generation: add 2 neurons
                remaining -= 2

    return generation


if __name__ == '__main__':
    # Read input
    n = int(input().strip())
    layer = []
    for _ in range(n):
        layer.append(int(input().strip()))

    # Calculate and print result
    result = findMinGeneration(layer)
    print(result)
