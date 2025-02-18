import numpy as np

if __name__ == '__main__':
    # =====================Basic Functions==========================
    print("====BASIC FUNCTIONS===")
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    # Note: Np arrays do not have ',' between the elements
    print(matrix)

    rows, cols = matrix.shape
    print(rows)
    print(cols)

    print(matrix[0][1])

    zeros_matrix = np.zeros((2, 2))
    print(zeros_matrix)

    ones_matrix = np.ones((6, 6))
    print(ones_matrix)

    full_matrix = np.full((4, 4), 5)
    print(full_matrix)

    identity = np.eye(5)
    print(identity)

    random_list = np.random.random((5,))
    random_matrix = np.random.random((5, 5))
    print(random_list)
    print(random_matrix)

    np_arrange = np.arange(5, 35, 10)
    my_arrange = [x for x in range(5, 35, 10)]
    print(np_arrange)
    print(my_arrange)

    # 10 elements spaced evenly between 5 and 35
    np_linspace = np.linspace(5, 35, 10)
    print(np_linspace)

    sub_matrix = matrix[:2, 1:3]
    print(sub_matrix)

    # Its by reference, so it will change in the original matrix
    sub_matrix[0, 1] = 99
    print(sub_matrix)
    print(matrix)

    first_row = matrix[0,]
    print(first_row)

    # Equivalent to [matrix[0,0], matrix[1,1], matrix[0,2]]
    print(matrix[[0, 1, 0], [0, 1, 2]])

    print(matrix[matrix % 2 == 0])

    #     ================Operations================
    print("====OPERATIONS===")

    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[7, 8, 9], [10, 11, 12]])
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)

    #     ================RESHAPE================
    print("====RESHAPE===")
    print(matrix.shape)
    print(matrix)
    print(matrix.reshape((3, 4)))
    print(matrix.reshape((-1)))
    print(matrix.reshape(6, -1))

    #     ================BROADCAST================
    print("====BROADCAST===")

    x = np.array([1])
    y = np.array([[10], [20]])

    print('shapes:', x.shape, '+', y.shape, '->', (x + y).shape, end='\n\n')
    print(x + y, end='\n\n')  # Низите се компатибилни.

    x = np.array([1, 2, 3])
    y = np.array([[10], [20]])

    print('shapes:', x.shape, '+', y.shape, '->', (x + y).shape, end='\n\n')
    print(x + y, end='\n\n')  # Низите се компатибилни.

    x = np.ones([3, 3, 2, 2, 1])
    y = np.ones([1, 2, 2, 2])

    print('shapes:', x.shape, '+', y.shape, '->', (x + y).shape, end='\n\n')
    print(x + y, end='\n\n')  # Низите се компатибилни.

    x = np.ones([3, 3, 2])
    y = np.array([[10], [20]])

    try:
        print('shapes:', x.shape, '+', y.shape, '->', (x + y).shape, end='\n\n')
        print(x + y)  # Последните димензии на `x` и `y` се 2 и 1 соодветно. Може да се прошират.
        # Претпоследните димензии на `x` и `y` се 3 и 2 соодветно. Не може да се прошират.
        # Значи низите не се компатибилни.
    except Exception as e:
        print(str(e))
