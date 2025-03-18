def rem_min_max(s):
    if len(s) < 2:
        return s
    s.remove(min(s))
    s.remove(max(s))
    return s

numbers = {1, 2, 3, 4, 5}
new= rem_min_max(numbers)
print(new)
