import numpy as np

''' Rod Cutting Problem
    Keane Pereira, 07 '''

def rod_cutting(prices, total_length):
    matrix = np.zeros((len(prices), total_length + 1))

    for i in range(1, len(prices)):
        for j in range(1, total_length + 1):
            
            if i < j:
                matrix[i][j] = max(matrix[i - 1][j], prices[i] + matrix[i][j - i])

            elif i > j:
                matrix[i][j] = matrix[i - 1][j]

            else:
                matrix[i][j] = max(matrix[i - 1][j], prices[i])

    print(matrix)
    return max(matrix[total_length])
    
prices = [0, 10, 24, 30, 40, 45]
total_length = 5
x = rod_cutting(prices, total_length)
print("Max: ", x)