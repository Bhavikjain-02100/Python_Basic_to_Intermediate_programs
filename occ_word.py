def count_words(s):
    words= s.split()
    w_count = {}
    for word in words:
        word = word.lower()
        if word in w_count:
            w_count[word] += 1
        else:
            w_count[word] = 1
    return w_count

strin = input("Enter a sentence: ")
print(count_words(strin))
