some_list = ["a", "b", "c", "d", "e", ]


def func_return_dict(a: list) -> dict:
    some_dict = {}
    for key, value in enumerate(a):
        some_dict[key] = value
    return some_dict


print(func_return_dict(some_list))
