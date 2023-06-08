import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    allowed_items = set("ABCD")
    if not set(skus).issubset(allowed_items):
        return -1

    item_a = len(list(re.finditer("A", skus)))
    item_b = len(list(re.finditer("B", skus)))
    item_c = len(list(re.finditer("C", skus)))
    item_d = len(list(re.finditer("D", skus)))

    price_a = item_a * 50
    price_b = item_b * 30
    price_c = item_c * 20
    price_d = item_d * 15

    if item_a % 3 == 0:
        price_a -= 20 * (item_a / 3)
    if item_b % 2:
        price_b -= 15 * (item_b / 2)

    return price_a + price_b + price_c + price_d




