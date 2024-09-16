scores = [96, 47, 113, 89, 100, 102]
count = 0

for element in scores:
    if element >= 100:
        scores.count(element)
        count += 1

print(count)

"""
Official answers:

count = 0

for score in scores:
    if score >= 100:
        count += 1

print(count)  # 3


high_scores = [score for score in scores if score >= 100]
print(len(high_scores)) # 3
"""
