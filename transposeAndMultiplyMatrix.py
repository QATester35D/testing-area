# Function to transpose a matrix
def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    print(len(matrix1[0]))
    print(len(matrix2))
    if len(matrix1[0]) != len(matrix2):
        return "Matrices cannot be multiplied"
    
    result = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

transposed_matrix1 = transpose_matrix(matrix1)
transposed_matrix2 = transpose_matrix(matrix2)

print("Transposed Matrix 1:", transposed_matrix1)
print("Transposed Matrix 2:", transposed_matrix2)

product = multiply_matrices(matrix1, matrix2)
print("Product of Matrix 1 and Matrix 2:", product)
