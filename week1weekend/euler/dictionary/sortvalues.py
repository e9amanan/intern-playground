def sort_by_values(d):

    return sorted(d.items(), key=lambda item: item[1], reverse=True)


data = {"a": 10, "b": 50, "c": 30}
print(sort_by_values(data))
