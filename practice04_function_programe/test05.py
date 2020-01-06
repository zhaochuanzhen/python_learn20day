def f1(*args):
    def sum():
        num = 0
        for n in args:
            num += n
        return num

    return sum()


f = f1(1, 3, 5, 7, 9)
print(f)
