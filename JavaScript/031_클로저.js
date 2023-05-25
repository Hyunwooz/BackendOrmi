`
def one(x):
    def two(y):
        return x ** y
    return two

승수2 = one(2)
승수3 = one(3)

승수2(3)
승수3(3)
`