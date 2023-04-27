def generate_combinations(s, index, current, result):
    if index == len(s):
        result.append(current)
        return

    # If the current character is a digit, skip it and move to the next character
    if s[index].isdigit():
        generate_combinations(s, index+1, current+s[index], result)
        return

    # Generate all possible combinations of upper and lower case for the current character
    generate_combinations(s, index+1, current+s[index].lower(), result)
    generate_combinations(s, index+1, current+s[index].upper(), result)


# Example usage
s = "a1b"
result = []
generate_combinations(s, 0, "", result)
print(result)

# Output
# ['a1b', 'a1B', 'A1b', 'A1B']
