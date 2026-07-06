def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


print(flatten_list([[1, 2], [3, 4, 5], [6]]))  