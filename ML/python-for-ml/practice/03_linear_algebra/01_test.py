u = [2, 2]
v = [4, 8]
z = [100, 200]

# sum vectors
result = [sum(t) for t in zip(u, v, z)]
print( result )

# scalar multiple on vector
alpha = 2
result_2 = [alpha * sum(t) for t in zip(u, v, z)]
print( result_2 )

# sum matrix
matrix_a = [
    [3, 6],
    [5, 9]
]
matrix_b = [
    [7, 9],
    [11, -3]
]
result_3 = [
    [sum(row) for row in zip(*t)] 
    for t in zip(matrix_a, matrix_b)
]
print( result_3 )

# matrix transpose
matrix_c = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_t = [
    [ele for ele in t]
    for t in zip(*matrix_c)
]
print(matrix_t)

matrix_aa = [
    [1, 1, 2],
    [2, 1, 1]
]
matrix_bb = [
    [1, 1],
    [2, 1],
    [1, 3]
]
result_p = [[
        sum(a * b for a, b in zip(row_a, column_b))
        for column_b in zip(*matrix_bb)
    ] for row_a in matrix_aa
]
print( result_p )