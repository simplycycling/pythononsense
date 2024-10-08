def contains(city, var_name):
    for v in var_name:
        if v == city:
            return True


destinations = [
    "Prague",
    "London",
    "Sydney",
    "Belfast",
    "Rome",
    "Aruba",
    "Paris",
    "Bora Bora",
    "Barcelona",
    "Rio de Janeiro",
    "Marrakesh",
    "New York City",
]

print(contains("Barcelona", destinations))
print(contains("Nashville", destinations))

"""
Official answer

def contains(element, lst):
    for item in lst:
        if item == element:
            return True

    return False

Or

def contains(element, lst):
    index = 0
    while index < len(lst):
        if lst[index] == element:
            return True

        index += 1
    
    return False
"""
