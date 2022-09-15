import time


def decorator(func):
    def make_some_sleep():
        counter = 3
        while counter > 0:
            time.sleep(1)
            print(counter)
            counter -= 1
        time.sleep(1)
        func()
    return make_some_sleep


@decorator
def what_time_is_it_now(*args, **kwargs):
    time_now = time.strftime("%H:%M:%S")
    print(time_now)


what_time_is_it_now()