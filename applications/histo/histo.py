"""
Algorithm very similar to word_count but with different input and output
"""

def show_hashes(count):
    # string to hold markings
    marks = ""
    # make "count" number of markings
    for i in range(count):
        marks += "#"
    
    return marks

def histo(f):
    file = open(f, "r")
    contents = file.read()
    # initialize a cache
    cache = {}
    # list of characters to ignore
    ignore = [",", ".", "!", "?", ":", ";", '"', "(", "/", ")", "-", "+", "=", 
              "/", "\\", "|", "[]", "{}", "()", "*", "^", "&", "\t", "\r", "\n"]
    # if character is in ignore list
    for i in ignore:
        # make ignored value into a space char
        contents = contents.lower().replace(i, " ")

    # make list of separate lowercased values
    words = contents.split(" ")
    # traverse through list
    for word in words:
        """ 
        From robin.txt:
        "IN MERRY ENGLAND in the time of old, ..."                "ignored"
                                                                     ||
        From words (after manipulation):                             \/
        ['in', 'merry', 'england', 'in', 'the', 'time', 'of', 'old', '', ... ]
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
    
    for k, v in cache.items():
        if len(k) > 14:
            print(k, " " + show_hashes(v))
        elif len(k) > 6:
            print(k, "\t", show_hashes(v))
        else:
            print(k, "\t\t", show_hashes(v))

histo("./robin.txt")