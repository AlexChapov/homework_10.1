import os
from functools import wraps


def log(filename: str):
    """Декоратор, который будет логировать вызов функции
    и ее результат в файл или в консоль."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                log_str = f"{func.__name__} ok. Result: {result}"
                return result

            except Exception as e:
                log_str = f"{func.__name__} {type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
                raise e

            finally:
                if filename:  # Запись лога в файл.
                    if not os.path.exists(r"logs"):
                        os.mkdir(r"logs")  # Создать папку «logs», если ее нет.
                    with open(os.path.join(r"logs", filename), "at") as file:
                        file.write(log_str + "\n")

                else:  # Вывод лога в консоль.
                    print(log_str)

        return inner

    return wrapper
