#!/usr/bin/env python3
"""Test cases for the neural network problem"""

from hackerrank_neural_network import findMinGeneration

def test_sample_case_0():
    """
    Sample Case 0:
    n = 3
    layer = [3, 3, 6]
    Expected output: 4
    """
    layer = [3, 3, 6]
    result = findMinGeneration(layer)
    print(f"Test Sample Case 0:")
    print(f"  Input: {layer}")
    print(f"  Output: {result}")
    print(f"  Expected: 4")
    print(f"  Status: {'PASS' if result == 4 else 'FAIL'}")
    print()
    return result == 4

def test_example_case():
    """
    Example from problem description:
    n = 4
    layer = [1, 1, 2, 4]
    Expected output: 6
    """
    layer = [1, 1, 2, 4]
    result = findMinGeneration(layer)
    print(f"Test Example Case:")
    print(f"  Input: {layer}")
    print(f"  Output: {result}")
    print(f"  Expected: 6")
    print(f"  Status: {'PASS' if result == 6 else 'FAIL'}")
    print()
    return result == 6

def test_all_equal():
    """Test case where all layers already equal"""
    layer = [5, 5, 5]
    result = findMinGeneration(layer)
    print(f"Test All Equal:")
    print(f"  Input: {layer}")
    print(f"  Output: {result}")
    print(f"  Expected: 0")
    print(f"  Status: {'PASS' if result == 0 else 'FAIL'}")
    print()
    return result == 0

def test_single_layer():
    """Test case with single layer"""
    layer = [10]
    result = findMinGeneration(layer)
    print(f"Test Single Layer:")
    print(f"  Input: {layer}")
    print(f"  Output: {result}")
    print(f"  Expected: 0")
    print(f"  Status: {'PASS' if result == 0 else 'FAIL'}")
    print()
    return result == 0

def test_two_layers():
    """Test case with two layers"""
    layer = [1, 2]
    result = findMinGeneration(layer)
    print(f"Test Two Layers:")
    print(f"  Input: {layer}")
    print(f"  Output: {result}")
    print(f"  Expected: 1")
    print(f"  Status: {'PASS' if result == 1 else 'FAIL'}")
    print()
    return result == 1

def trace_example():
    """Trace through the sample case to verify logic"""
    layer = [3, 3, 6]
    target = max(layer)
    deficits = [target - x for x in layer]

    print("Trace Sample Case [3, 3, 6]:")
    print(f"  Target: {target}")
    print(f"  Deficits: {deficits}")
    print()

    generation = 0
    for i, deficit in enumerate(deficits):
        if deficit == 0:
            print(f"  Layer {i}: deficit=0, skip")
            continue

        print(f"  Layer {i}: deficit={deficit}")
        remaining = deficit
        start_gen = generation

        while remaining > 0:
            generation += 1
            add = 1 if generation % 2 == 1 else 2
            before = remaining
            remaining -= add
            gen_type = "odd" if generation % 2 == 1 else "even"
            print(f"    Gen {generation} ({gen_type}): add {add}, remaining: {before} -> {max(0, remaining)}")

        print(f"  Layer {i} complete: used generations {start_gen+1} to {generation}")
        print()

    print(f"  Total generations: {generation}")
    print()

if __name__ == '__main__':
    print("=" * 60)
    print("Testing HackerRank Neural Network Problem")
    print("=" * 60)
    print()

    # Run trace first
    trace_example()

    # Run all tests
    tests = [
        test_sample_case_0,
        test_example_case,
        test_all_equal,
        test_single_layer,
        test_two_layers
    ]

    results = [test() for test in tests]

    print("=" * 60)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 60)
