def funA(x):
    def funB(y):
        return x+y
    return funB

fun = funA(5)
print(fun(3))