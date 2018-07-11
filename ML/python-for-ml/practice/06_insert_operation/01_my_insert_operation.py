'''
https://www.acmicpc.net/problem/14888
'''

def calculate(val1, val2, mode):
    if mode == 0: # +
        return val1 + val2
    elif mode == 1: # -
        return val1 - val2
    elif mode == 2: # *
        return val1 * val2
    else: # //
        if val1 < 0:
            return -((-val1) // val2)
        else:
            return val1 // val2


def make_result(oper_list):
    global num_list
    result = calculate(num_list[0], num_list[1], oper_list[0])

    for i in range(1, len(oper_list)):
        result = calculate(result, num_list[i+1], oper_list[i])

    return result


v_min = None
v_max = None
def make_oper_list(oper_num_list, index=0, oper_list=list()):
    global v_min
    global v_max
    global num_cnt
    if index == 0:
        oper_list = [-1 for _ in range(num_cnt - 1)]

    for i in range(4):
        if oper_num_list[i] > 0:
            oper_num_list[i] -= 1
            oper_list[index] = i
            
            if index + 2 == num_cnt:
                result = make_result(oper_list)
                if v_min == None:
                    v_min = result
                if v_max == None:
                    v_max = result
                if v_min > result:
                    v_min = result
                if v_max < result:
                    v_max = result
                oper_num_list[i] += 1
                continue

            make_oper_list(oper_num_list, index + 1, oper_list)
            oper_num_list[i] += 1



num_cnt = int(input())
num_list = [int(ele) for ele in input().split(' ')]

oper_num_list = [int(ele) for ele in input().split(' ')]
make_oper_list(oper_num_list)

print(v_max)
print(v_min)