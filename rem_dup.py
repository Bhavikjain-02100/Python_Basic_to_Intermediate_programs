def rem_dup(s):
    result = ""
    for char in s:
        if char not in result:
            result+=char
    return result

# Example usage
strin = input("Enter a string: ")
print(rem_dup(strin))
