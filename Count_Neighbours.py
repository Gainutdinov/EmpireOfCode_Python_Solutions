def count_neighbours(grid, row, col):
    indexes = [(row-1, col-1),(row-1, col),(row-1, col+1),
               (row, col+1),               (row, col-1),
               (row+1, col-1),(row+1, col),(row+1, col+1),]
    neighbor_counter = 0
    for x, y in indexes:
        if x >= 0 and y >= 0:
            try:
                neighbor_counter += grid[x][y]
            except IndexError:
                pass
    return neighbor_counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
