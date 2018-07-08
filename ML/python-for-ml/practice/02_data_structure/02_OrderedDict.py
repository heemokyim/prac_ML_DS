from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500
print(type(d), d)
for k, v in d.items():
    print(k, v)

dd = dict()
dd['x'] = 100
dd['y'] = 200
dd['z'] = 300
dd['l'] = 500
print(type(dd), dd)
for k, v in dd.items():
    print(k, v)


# lambda를 이용한 OrderedDict key or value sorting
print('lambda key sorting')
for k, v in OrderedDict(sorted(
    d.items(),
    key=lambda t: t[0])).items():
    print(k, v)

print('lambda value sorting')
for k, v in OrderedDict(sorted(
    d.items(),
    key=lambda t: t[1])).items():
    print(k, v)
    