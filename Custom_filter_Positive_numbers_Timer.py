from datetime import datetime


def my_filter(func, iterable):
    """

    :param func:
    :param iterable:
    :return: list
    """
    return (i for i in iterable if func(i))


def get_positive_numbers():
    user_numbers = input("Insert numbers separate by ,: ")
    numbers_list = list(map(int, user_numbers.split(",")))
    return list(my_filter(lambda x: True if x > 0 else False, numbers_list))


def timeit(func):
    """
    This function is a decorator to check runtime of a function.
    :param func: decorator on a given function
    :return: wrapper_function decorator
    """
    def wrapper_function(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        print(f" Run time of the function {func.__name__} with runtime: {end - start}.")
    return wrapper_function


@timeit
def timer(func, *args):
    """
        This function is a decorator to check runtime of a function.
        :param func: decorator on a given function
        :return: wrapper_function decorator
        """

    func(*args)


if __name__ == "__main__":
    print(get_positive_numbers())
    timer(print, "Hello")
    timer(zip, [1, 2, 3], [4, 5, 6])
    timer("Hi {name}".format, name="Bug")

