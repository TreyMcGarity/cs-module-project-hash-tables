def word_count(s):
    # initialize a cache
    cache = {}
    # list of characters to ignore
    ignore = [",", ".", "!", "?", ":", ";", '"', "(", "/", ")", "-", "+", "=", 
              "/", "\\", "|", "[]", "{}", "()", "*", "^", "&", "\t", "\r", "\n"]
    # if character is in ignore list
    for i in ignore:
        # make ignored value into a space char
        s = s.lower().replace(i, " ")

    # make list of separate lowercased values
    words = s.split(" ")
    print(words[:5])
    # traverse through list
    for word in words:
        """ 
        From line 39:
        "Hello, my cat. ..."                   "ignored"        "ignored"
                                                  ||               ||
        From words (after manipulation):          \/               \/
                                        ['hello', '', 'my', 'cat', '', ...]
        """
        # hit a removed ignored element
        if word == "":
            # do nothing but keep traversing
            continue
        if word in cache:
            # increment count of word
            cache[word] += 1
        else:
            # add word to cache
            cache[word] = 1
            
    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))