from pprint import pprint

# enumerate #

''' enumerate
list 의 element를 추출할 때 번호랑 같이 붙여서 추출
'''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

mylist = 'abcde'
print( list(enumerate(mylist)) )


mydict = {i:j for i, j in enumerate(mylist)}
pprint(mydict)


# zip
'''
두 개의 리시트의 값을 병렬적으로 추출함
'''
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

for i, (a, b) in enumerate(zip(alist,blist)):
    print(i, a, b)

a, b, c = zip(
    (1, 2, 3),
    (10, 20, 30),
    (100, 200, 300)
)
print(a, b, c)
print( [sum(x) for x in zip(a, b, c)] )