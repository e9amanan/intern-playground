def swap_keys_values(d):
    return {value: key for key, value in d.items()}


original = {'a': 1, 'b': 2, 'c': 3}
print(swap_keys_values(original))  