def remove_duplicates(items):
    return list(dict.fromkeys(items))


print(remove_duplicates([3, 1, 2, 3, 2, 4, 1])) 