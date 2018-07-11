import itertools # permutations() : 모든 경우의 조합 생성
from functools import reduce # 앞의 funtion으로 iterable collection을 하나로 줄여줌

# itertools.permutations()
# : iterable에 대한 모든 조합들을 다 뽑아줌
# print(list(itertools.permutations('ABCD')))

def insert_operation(length, input_num, input_oper):

    ops = {
        0: (lambda x, y: x + y),
        1: (lambda x, y: x - y),
        2: (lambda x, y: x * y),
        3: (lambda x, y: x // y if x > 0 else -((-x) // y))
    }
    oper_permutation = []
    result = []
    list(oper_permutation.extend(
        [index] * value
        ) for index, value in enumerate(input_oper) if value > 0)
    #print(oper_permutation)
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    #pprint(permutation)
    for i in permutation:
        result.append(reduce(lambda x,y: ops[i.pop()](x, y), input_num))
    
    print(max(result))
    print(min(result))


n = int(input())
input_num = [int(x) for x in input().split(' ')]
input_oper = [int(x) for x in input().split(' ')]
insert_operation(n, input_num, input_oper)