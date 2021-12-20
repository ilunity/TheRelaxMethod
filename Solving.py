INITIAL_NUMBER = 1


def convert_matrix_for_relax_method(A, B, N):
    b_matrix = []
    c_matrix = []
    for i in range(N):
        b_matrix.append([])
        for j in range(N):
            b_ij = -1 * (A[i][j] / A[i][i])
            b_matrix[i].append(b_ij)

        c_i = (B[i] / A[i][i])
        c_matrix.append(c_i)

    return b_matrix, c_matrix


def generate_initial_array(array_size):
    initial_array = []
    for i in range(array_size):
        initial_array.append(INITIAL_NUMBER)

    return initial_array


def index_of_max_abs_value(array):
    max_value = -1
    for i in range(len(array)):
        if abs(array[i]) > max_value:
            max_value = abs(array[i])
            index_of_max = i

    return index_of_max


def update_R_array(B, C, X, array_size):
    R = []
    for i in range(array_size):
        new_value = C[i] - X[i]
        for j in range(array_size):
            if i != j:
                new_value += B[i][j] * X[j]
        R.append(new_value)

    return R


def is_accuracy_achieved(R, eps):
    for i in range(len(R)):
        if abs(R[i]) >= eps:
            return False

    return True


def relax(B, C, array_size, eps):
    X = generate_initial_array(array_size)
    R = update_R_array(B, C, X, array_size)

    k = 0
    while (not is_accuracy_achieved(R, eps)):
        i = index_of_max_abs_value(R)
        X[i] += R[i]
        R = update_R_array(B, C, X, array_size)
        k += 1

    print(k)
    return X


def check_answer(A, X, array_size):
    for i in range(array_size):
        value = 0
        for j in range(array_size):
            value += A[i][j] * X[j]

        print(f'Значение {i}-го уравнения: {value}')


if __name__ == "__main__":
    A = [[-10, -2, -2], [-1, 10, -2], [-1, -1, 10]]
    b = [6, 7, 8]
    array_size = 3
    eps = 0.0001

    B, C = convert_matrix_for_relax_method(A, b, array_size)
    X = relax(B, C, array_size, eps)

    check_answer(A, X, array_size)
