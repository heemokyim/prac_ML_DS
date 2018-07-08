# join #
colors = ['a', 'uko', '333333', '1234']
result = '/ /'.join(colors)
print(result)

# split #
items = 'zero one two three'.split()
print(items)

example = 'python,jquery,javascript'
print(example.split(","))

a, b, c = example.split(",") # unpacking
print(a, b, c)

example = 'cs50.gachon.edu'
subdomain, domain, tld = example.split(".")
print(subdomain, domain, tld)