# cost = [[0, 1, 8], [9, 0, 5], [1, 7, 0]]
# Enter matrix size: 4
# Enter row: 0 3 inf 5
# Enter row: 2 0 inf 4
# Enter row: inf 1 0 inf
# Enter row: inf inf 2 0
n = int(input("Enter matrix size: "))
D = [[]] * n

for i in range(n):
    D[i] = list(map(lambda x: 999 if x == "inf" else int(x), input("Enter row: ").split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

print("Final Shortest Path Matrix")
for i in range(n):
    print(*D[i])
