from pprint import pprint

result = [i for i in range(10)]
print(result)

result2 = [i for i in range(10) if i % 3 == 0]
print(result2)

word_1 = "Hello!"
word_2 = "World?"
result3 = [i + j for i in word_1 for j in word_2]
'''
for i in word_1:
    for j in word_2:
        result3.append(i + j)
'''
print(result3)

# cartesian product
case_1 = "ABC"
case_2 = "DEA"
result4 = [i + j for i in case_1 for j in case_2 if i != j]
result4.sort()
print(result4)

# 2-demension list
words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [ [w.upper(), w.lower(), len(w)] for w in words]
pprint(stuff)