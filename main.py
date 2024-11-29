# matrix sample
matrix = [[5,3,2,1],[1,2,10,1],[4,3,2,20],[2,1,2,1]]

def main(matrix):
    buckets = 0
    index_matrix = 0
    index_matrix_row = 0
    for mat in matrix:
        index_row = 0
        for val in mat:
            if index_matrix_row > index_row:
                index_row += 1
                continue
            buckets += val
            if index_row < len(mat):
                if index_row+1 == len(mat):
                    break
                if mat[index_row+1] <= matrix[index_matrix][index_row-1]:
                    break
            index_row += 1
            index_matrix_row += 1
        index_matrix += 1
    return buckets

buckets = main(matrix)

print(f"{buckets} buckets")
