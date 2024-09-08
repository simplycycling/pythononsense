def capitate(string):
    words = string.split(" ")
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())

    return " ".join(capitalized_words)


string = "launch school tech & talk"
print(capitate(string))


"""
An easier way would be 

def capitate(string):
    return string.title()
"""
