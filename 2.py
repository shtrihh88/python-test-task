from functools import wraps


def cls_method_decorator(param: int):

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            increment = self.increment_var(param, *args, **kwargs)
            return increment

        return wrapper

    return decorator


class SomeClass:
    some_var: int

    def __init__(self, some_var: int):
        self.some_var = some_var

    def increment_var(self, increment: int):
        self.some_var += increment

    @cls_method_decorator(param=30)
    def some_func(self, condition=None):
        print(self.some_var)

    def print_var(self):
        print(self.some_var)

    """
    Вам дан класс SomeClass, содержащий целочисленную переменную some_var
    У него есть вспомогательный метод 'increment_var', 
    увеличивающий значение данной переменной (some_var) на указанную величину
    
    Ваша задача заключается в том, чтобы реализовать декоратор (cls_method_decorator) 
    Внутри он должен модифицировать some_var через вызов increment_var с указанным декоратору значением
    
    
    """


if __name__ == '__main__':
    cls = SomeClass(20)
    cls.print_var()

    cls.some_func()
