def get_pascal_triangle(num):

    for i in range(num):
        value = 1
        for j in range(i + 1):
            print(value, end=" ")
            value = value * (i - j) // (j + 1)
        print()