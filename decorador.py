
from inspect import ArgSpec

from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG


def fun(funcion):
    def fun(*args, **kwargs):
        print("Primer decorador")
    return fun()

@primer_d
def funcion():
    print("Mi primer decorador")

