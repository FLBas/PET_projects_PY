def get_scalar():
    vector1 = input().split()
    vector2 = input().split()

    res = 0

    for i in range(len(vector1)):
        res += float(vector1[i]) * float(vector2[i])

    return res
