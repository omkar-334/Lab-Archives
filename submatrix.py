import numpy as np

def find_largest_contiguous_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0, 0, 0, 0  # Return default values if the matrix is empty

    rows = len(matrix)
    cols = len(matrix[0])

    matrix = np.array(matrix)

    # Variables to store the result
    max_size = 0
    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0

    # Initialize a 2D array to store the height of the submatrix ending at each cell
    dp = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                # Calculate the height of the submatrix ending at this cell
                dp[i, j] = dp[i - 1, j] + 1 if i > 0 else 1

        # Stack to maintain indices of heights
        stack = []
        for j in range(cols):
            while stack and dp[i, j] < dp[i, stack[-1]]:
                height = dp[i, stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                size = height * width
                if size > max_size:
                    max_size = size
                    start_row = i - height + 1
                    start_col = stack[-1] + 1 if stack else 0
                    end_row = i
                    end_col = j - 1

            stack.append(j)

        while stack:
            height = dp[i, stack.pop()]
            width = cols if not stack else cols - stack[-1] - 1
            size = height * width
            if size > max_size:
                max_size = size
                start_row = i - height + 1
                start_col = stack[-1] + 1 if stack else 0
                end_row = i
                end_col = cols - 1

    return start_row, start_col, end_row, end_col

# Example usage:
binary_matrix = [[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]]


start_row, start_col, end_row, end_col = find_largest_contiguous_submatrix(binary_matrix)

print(f"Largest Contiguous Submatrix:")
for i in range(start_row, end_row + 1):
    print(binary_matrix[i][start_col:end_col + 1])
