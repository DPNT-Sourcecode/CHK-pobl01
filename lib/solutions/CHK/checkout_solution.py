import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_a = len(list(re.finditer("A", skus)))
    item_b = len(list(re.finditer("B", skus)))
    item_c = len(list(re.finditer("C", skus)))
    item_d = len(list(re.finditer("D", skus)))

    price_a = item_a * 50
    price_b = item_b * 30
    price_c = item_c * 20
    price_d = item_d * 50


