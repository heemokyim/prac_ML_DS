from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)

deque_list.appendleft(90)
print(deque_list)
print(deque_list.pop())
print(deque_list)
