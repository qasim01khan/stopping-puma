def find_max_sum(strings):
    max_sum = 0
    for s in strings:
        current_sum = 0
        for char in s:
            if char.isdigit():
                current_sum += int(char)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
# Example usage
if __name__ == "__code__":
    input_strings = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
    result = find_max_sum(input_strings)
    print("Max digit sum:", result)  # Output should be 13
