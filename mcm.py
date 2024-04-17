import sys

def matrix_chain_order(p, i, j):
    if i == j:
        return 0

    min_cost = sys.maxsize
    
    for k in range(i, j):
        count = (matrix_chain_order(p, i, k) +
                 matrix_chain_order(p, k + 1, j) +
                 p[i-1] * p[k] * p[j])

        if count < min_cost:
            min_cost = count
    
    return min_cost

# Dynamic input for matrix dimensions
n = int(input("Enter the number of matrices: "))
matrix_dims = list(map(int, input("Enter the dimensions of matrices separated by spaces: ").split()))

# Calculate minimum number of multiplications
min_multiplications = matrix_chain_order(matrix_dims, 0, n - 1)

# Output result
print("Minimum number of multiplications is", min_multiplications)
