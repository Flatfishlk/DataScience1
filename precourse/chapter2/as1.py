import numpy as np
def one(x):
    return np.arange(x)

# print one(100)

def two():
    return np.linspace(0, 50, 100).reshape(100, 1)
# print two()

def three():
    return np.arange(36).reshape(6,6)
# print three()

def four():
    return np.random.randint(10, size=(2,3))
# print four()

def five():
    return np.identity(6)
# print five()

def six():
    return np.arange(100).reshape(10,10)
# print six()

def seven():
    m = six()
    return m[:, :3]
# print seven()

def eight():
    m = six()
    return m[8:,:]
# print eight()

def nine():
    v = np.arange(0,10,1).reshape(1,10)
    return v
# print nine()

def ten():
    v = nine()
    return v + 0.5
# print ten()

def eleven():
    v = nine()
    return v * -2
# print eleven()

def twelve():
    v = nine()
    B = np.ones((1,10))*0.5
    return v + B
# print twelve()

def thirteen():
    column_vector = [[3],[2],[1]]
    row_vector = [1,2,3]
    square_matrix = [[3,3,3],[2,2,2],[1,1,1]]
    return column_vector, row_vector, square_matrix
# print thirteen()

column_vector = np.arange(3).reshape(3,1)
row_vector = np.arange(3).reshape(1,3)
square_matrix = np.arange(9).reshape(3,3)

def fourteen():
    return column_vector * row_vector
# print fourteen()

def fifteen(column_vector, row_vector, square_matrix):
    c_answer = np.dot(square_matrix, column_vector)
    r_answer = np.dot(row_vector, square_matrix)
    return c_answer, r_answer
# print fifteen(column_vector, row_vector, square_matrix)

def sixteen(column_vector, row_vector):
    return np.dot(row_vector, column_vector)
# print sixteen(column_vector, row_vector)

def seventeen():
    A = (3, 2)
    B = (4, 3)
    if A[1] == B[0]:
        answer_one = True
        answer_two = (A[0], B[1])
    else:
        answer_one = False
        answer_two = None

    if B[1] == A[0]:
        answer_three = True
        answer_four = (B[0], A[1])
    else:
        answer_three = False
        answer_four = None
    return answer_one, answer_two, answer_three, answer_four
# print seventeen()

def eighteen():
    rand_matrix = np.random.randint(18, size=(3,6))
    answer_one = np.dot(rand_matrix, rand_matrix.T)
    return answer_one

# print eighteen()

def nineteen():
    A = np.random.randint(20, size=(6,2))
    B = np.random.randint(20, size=(6,2))
    answer_square = A*A
    answer_add = A + B
    answer_subtract = A - B
    answer_multiply = A * B
    answer_divide = A / B
    return answer_square, answer_add, answer_subtract, answer_multiply, answer_divide
# print nineteen()

def twenty():
    A = np.arange(1,5,1).reshape(4,1)
    B = np.linspace(100,300,3).reshape(1,3)
    answer = np.add(A, B)
    return answer
# print twenty()

def twenty_one():
    M = np.linspace(0,99,100).reshape(10,10)
    return M
# print twenty_one()

def twenty_two():
    M_sum = twenty_one().sum()
    M_mean = twenty_one().mean()
    M_std = twenty_one().std()
    return M_sum, M_mean, M_std
# print twenty_two()

def twenty_three():
    col_sum = np.sum(twenty_one(), axis = 0)
    col_mean = np.mean(twenty_one(), axis = 0)
    col_std = np.std(twenty_one(), axis = 0)
    return col_sum, col_mean, col_std
# print twenty_three()

def twenty_four():
    row_sum = np.sum(twenty_one(), axis = 1)
    row_mean = np.mean(twenty_one(), axis = 1)
    row_std = np.std(twenty_one(), axis = 1)
    return row_sum, row_mean, row_std
print twenty_four()
