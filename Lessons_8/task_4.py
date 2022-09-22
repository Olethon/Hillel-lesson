import time


def countdown_decorator(func):
    def wrapper(*args, **kwargs):
        counter = 3
        while counter > 0:
            time.sleep(1)
            print(counter)
            counter -= 1
        time.sleep(1)
        func(*args, **kwargs)
    return wrapper


@countdown_decorator
def what_time_is_it_now():
    time_now = time.strftime("%H:%M:%S")
    print(time_now)


what_time_is_it_now()