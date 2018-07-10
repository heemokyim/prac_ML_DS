def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x
        for x in [len(vector) for vector in vector_variables[1:]])

## all => iterable을 받아 그중 하나라도 False 면 False
## 아니면 True가 나옴

print("01. vector_size_check ")
print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False
print()

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(tube) for tube in zip(*vector_variables)]

print("02. vector_addition")
print(vector_addition([1, 3], [2, 4], [6, 7])) # Expected value: [9, 14]
print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
#print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError
print()

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2 - sum(elements) for elements in zip(*vector_variables)]

# 실행결과
print("03. vector subtraction")
print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]
print()

def scalar_vector_product(alpha, vector_variable):
    return [alpha * data for data in vector_variable]

# 실행결과
print("04. scalar vector product")
print(scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
print(scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print(scalar_vector_product(4,[1])) # Expected value: [4]
print()

def matrix_size_check(*matrix_variables):
    pivot_row = len(matrix_variables[0])
    pivot_col = len(matrix_variables[0][0])
    return all([
        True
        if pivot_row == len(temp_matrix) and pivot_col == len(temp_matrix[0])
        else False
        for temp_matrix in matrix_variables[1:]
    ])

# 실행결과
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print("05. matrix size check")
print(matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
print(matrix_size_check(matrix_y, matrix_z)) # Expected value: True
print(matrix_size_check(matrix_x, matrix_w)) # Expected value: True
print()


def is_matrix_equal(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        return False
    pivot_matrix = matrix_variables[0]
    pivot_row = len(matrix_variables[0])
    pivot_col = len(matrix_variables[0][0])

    return all([
        True if pivot_matrix[row][col] == temp_matrix[row][col]
        else False
            for temp_matrix in matrix_variables[1:]
            for row in range(pivot_row)
            for col in range(pivot_col) 
    ])

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]

print("06. is matrix equal")
print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
print(is_matrix_equal(matrix_x, matrix_x)) # Expected value: True
print()


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [
        [sum(row) for row in zip(*same_row)]
        for same_row in zip(*matrix_variables)
    ]

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print("07. matrix addition")
print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]
print()


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [
        [row[0] * 2 - sum(row) for row in zip(*same_row)]
        for same_row in zip(*matrix_variables)
    ]

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print("08. matrix subtraction")
print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]
print()


def matrix_transpose(matrix_variable):
    return [ list(col_list) for col_list in zip(*matrix_variable) ]

# 실행결과
matrix_w = [[2, 5], [1, 1], [2, 2]]

print("09. matrix transpose")
print(matrix_transpose(matrix_w))
print()

def scalar_matrix_product(alpha, matrix_variable):
    return [
        [alpha * element for element in elements]
        for elements in matrix_variable
    ]

# 실행결과
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print("10. scalar_matrix_product")
print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
print(scalar_matrix_product(3, matrix_w)) #Expected value: [[6, 15], [3, 3], [6, 6]]
print()

def is_product_availability_matrix(matrix_a, matrix_b):
    if type(matrix_a) != list or type(matrix_b) != list:
        return False
    return all(
        len(row_a) == len(col_list_b)
        for row_a in matrix_a
        for col_list_b in zip(*matrix_b)
    )

# 실행결과
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]
matrix_w = None

print("11. is product availability matrix")
print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True
print()

def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        return False
    return [
        [
            sum([row_a[i] * v for i, v in enumerate(col_b)])
            for col_b in zip(*matrix_b)
        ]
        for row_a in matrix_a
    ]

# 실행결과
matrix_x = [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print("12. matrix product")
print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
print(matrix_product(matrix_z, matrix_w)) # Expected value: False
print()