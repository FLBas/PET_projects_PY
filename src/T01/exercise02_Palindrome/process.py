def get_palindrome():
    num = input()

    res = True

    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            res = False
        
    return res

123321