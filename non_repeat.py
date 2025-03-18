def frst_non_rep_chr(s):
    char_count = {}
    for i in s:
        char_count[i] = char_count.get(i, 0) + 1
    for i in s:
        if char_count[i] == 1:
            return i
    return None

strin = input("Enter a string: ")
result = frst_non_rep_chr(strin)

if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found.")
