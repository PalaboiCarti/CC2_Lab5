#nov/3/2023
#unspeakable fuckery 

def get_word():
    input_string = input("Input words: ")
    words = input_string.split()
    return words
    
words = get_word()

def matcher(words):
    matching_words = {}

    for word in words:
        key = word[-3:]
        if key in matching_words:
            print(f"{word} added into {matching_words}")
            matching_words[key].append(word)
        else:
            matching_words[key] = [word]
            print(f"Key {matching_words[key]} has been made")
            print(matching_words)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    for key, match in matching_words.items():
        print(f"array of {key}: {match}")

matcher(words)
