def longest_unique_substring(s):
    start = 0
    max_length = 0
    max_substr = ""
    seen = {}
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_substr = s[start:i + 1]
    print(max_substr)
input_string = input("Enter a string: ")
longest_unique_substring(input_string)
