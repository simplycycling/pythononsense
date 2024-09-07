def is_empty_or_blank(s):
    return not s or s.isspace()


print(is_empty_or_blank("mars"))  # False
print(is_empty_or_blank("  "))  # True
print(is_empty_or_blank(""))  # True

"""
Official method:

def is_empty_or_blank(s):
    return s.strip(' ') == ''

or

def is_empty_or_blank(s):
    return len(s.strip(' ')) == 0
"""
