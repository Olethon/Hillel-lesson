some_list = ["a", "b", "c", "d", "e", ]


def func_return_dict(a: list) -> dict:
    index_list = [key for key, value in enumerate(a)]
    return dict(zip(index_list, a))


print(func_return_dict(some_list))
