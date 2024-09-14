def first(list):
    if len(list) == 0:
        return "List is empty"
    else:
        return list[0]


print(first(["Earth", "Moon", "Mars"]))

"""
Official answer:

def first(lst):
    if lst:
        return lst[0]
    else:
       return None
"""
