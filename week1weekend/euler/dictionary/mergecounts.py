from collections import Counter

def merge_inventories(inv1, inv2):
    return dict(Counter(inv1) + Counter(inv2))

inv_a = {'apples': 10, 'bananas': 5}
inv_b = {'bananas': 12, 'oranges': 8}
print(merge_inventories(inv_a, inv_b))