import numpy as np

def read_matrix(name):
    mat = []
    print(f"Enter elements of {name} 3x3 matrix:")
    for i in range(3):
        row = list(map(int, list(input(f"Row {i+1}: "))))
        if len(row) != 3:
            print("Each row must have exactly 3 digits. Try again.")
            return read_matrix(name)
        mat.append(row)
    return np.array(mat)

a = read_matrix("first")
b = read_matrix("second")
c = read_matrix("third")

res = np.matmul(np.matmul(a, b), c)

print("Multiplication of the matrices:")
for row in res:
    print(*row)
