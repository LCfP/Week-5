from exercises_5_3_23.vectors import add_vectors, scalar_mult, dot_product

print(
    add_vectors([1, 1], [1, 1]) == [2, 2] and
    add_vectors([1, 2], [1, 4]) == [2, 6] and
    add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4] and

    scalar_mult(5, [1, 2]) == [5, 10] and
    scalar_mult(3, [1, 0, -1]) == [3, 0, -3] and
    scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14] and

    dot_product([1, 1], [1, 1]) ==  2 and
    dot_product([1, 2], [1, 4]) ==  9 and
    dot_product([1, 2, 1], [1, 4, 3]) == 12
)
