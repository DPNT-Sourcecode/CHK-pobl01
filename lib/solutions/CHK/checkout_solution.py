import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_a = len(list(re.finditer("A", skus)))
    item_b = len(list(re.finditer("B", skus)))
    item_c = len(list(re.finditer("C", skus)))
    item_d = len(list(re.finditer("D", skus)))

