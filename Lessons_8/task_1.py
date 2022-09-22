coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def two_tuple_in_dict(cortege_1: tuple, cortege_2: tuple) -> dict:
    return dict(zip(cortege_1, cortege_2))


print(two_tuple_in_dict(coin, code))
