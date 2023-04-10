matrix = [[2, 5, 6, 7],
          [2, 4, 8, 9],
          [6, 7, 5, 9],
          [3, 2, 1, 4]]

sum_even = matrix[0][0] + matrix[0][2] + matrix[1][0] + matrix[1][1] + matrix[1][2] + matrix[2][0] + matrix[3][1] + matrix[3][3]
print(sum_even)

sum_odd = matrix[0][1] + matrix[0][3] + matrix[1][3] + matrix[2][1] + matrix[2][2] + matrix[2][3] + matrix[3][0] + matrix[3][2]
print(sum_odd)

sum_under_main = matrix[1][0] + matrix[2][0] + matrix[2][1] + matrix[3][0] + matrix[3][1] + matrix[3][2]
print(sum_under_main)

sum_over_second = matrix[0][1] + matrix[0][2] + matrix[0][3] + matrix[1][2] + matrix[1][3] + matrix[2][3]
print(sum_over_second)

mean_main = (matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3]) / 4
print(mean_main)

mean_second = (matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0]) / 4
print(mean_second)