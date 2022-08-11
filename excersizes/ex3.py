import logging
import time

logger = logging.getLogger(__name__)

logger.setLevel("INFO")
handler = logging.StreamHandler()
logger_string_format = "%(asctime)s -- %(levelname)s --- %(message)s"
formatter = logging.Formatter(logger_string_format)
handler.setFormatter(formatter)
logger.addHandler(handler)


def cacher(func):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]

    return inner


def process_timer(func):
    def inner(n):
        start = time.time()
        result = func(n)
        end = time.time()
        logger.debug(f"{func.__name__} ran in {end - start, 2}s")
        return result

    return inner


@process_timer
@cacher
def fibonachi(number):
    if number <= 1:
        return number
    return fibonachi(number - 1) + fibonachi(number - 2)


@process_timer
@cacher
def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


print(fibonachi(10))
