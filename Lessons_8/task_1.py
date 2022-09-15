coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def two_tuple_in_dict(cortege_1: tuple, cortege_2: tuple) -> dict:
    output_dict = dict(zip(cortege_1, cortege_2))
    return output_dict


print(two_tuple_in_dict(coin, code))
