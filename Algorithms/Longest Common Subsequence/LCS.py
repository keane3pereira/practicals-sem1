import numpy as np

### Longest Common Subsequence

L1 = list("KEANE07")
L2 = list("KEEEN7")
print(f"L1: {L1} \nL2: {L2}")

array = np.zeros((len(L1) + 1, len(L2) + 1))

for i in range(1, len(L1) + 1):
    for j in range(1, len(L2) + 1):
        if L1[i - 1] == L2[j - 1]:
            array[i][j] = array[i - 1][j - 1] + 1
        else:
            array[i][j] = max(array[i - 1][j], array[i][j - 1])

print(array)
print(array[-1][-1])
