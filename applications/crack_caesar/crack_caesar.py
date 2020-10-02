# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

def decode_cipher(f):
    file = open(f, "r")
    contents = file.read()

    cache = {}
    word_count = 0

    for character in contents:
        if character.isalpha() != True:
            continue
        # if char isn't in cache add it
        if character not in cache:
            cache[character] = 1
        # otherwise, increment value at key 
        else:
            cache[character] += 1

        word_count += 1

    for item in cache:
        cache[item] = round((cache[item] / word_count) * 100, 2)

    key_value = sorted(list(cache.items()), key = lambda item: item[1], reverse = True)

    print(key_value) #returns list of tuples of most to least frequent characters
    return 

    
decode_cipher("./ciphertext.txt")