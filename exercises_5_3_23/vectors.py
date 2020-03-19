def add_vectors(vector1, vector2):
    if not len(vector1) == len(vector2):
        return None

    vector3 = []
    for elem_a, elem_b in zip(vector1, vector2):        # zip is like enumerate (p117) but for combining lists
        vector3.append(elem_a + elem_b)

    return vector3


def scalar_mult(scalar, vector):
    new_vector = []
    for element in vector:
        new_vector.append(scalar * element)

    return new_vector


def dot_product(vector1, vector2):
    if not len(vector1) == len(vector2):
        return None

    sum = 0
    for elem_a, elem_b in zip(vector1, vector2):        # zip is like enumerate (p117) but for combining lists
        sum += elem_a * elem_b

    return sum
