grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def numIslands(G) -> int:
    # Scan the matrix
    numRows = len(G)
    numCols = len(G[0])
    result = 0

    for y in range(numRows):
        for x in range(numCols):
            elem = G[y][x]
            if elem == "1":
                result += 1
                markAsZerosFromHere(y, x, G)

    return result


def markAsZerosFromHere(r, c, A):
    if r < 0 or r > len(A) - 1 or c < 0 or c > len(A[0]) - 1 or A[r][c] == "0":
        return

    A[r][c] = "0"
    markAsZerosFromHere(r - 1, c, A)
    markAsZerosFromHere(r + 1, c, A)
    markAsZerosFromHere(r, c - 1, A)
    markAsZerosFromHere(r, c + 1, A)


print(numIslands(grid2))
