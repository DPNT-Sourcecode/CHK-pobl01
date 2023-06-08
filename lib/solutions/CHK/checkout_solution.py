import re

def find_sku(sku, skus):
    return len(list(re.finditer(sku, skus)))

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    allowed_items = set("ABCD")
    if not set(skus).issubset(allowed_items):
        return -1

    item_a = find_sku("A", skus)
    item_b = find_sku("B", skus)
    item_c = find_sku("C", skus)
    item_d = find_sku("D", skus)

    price_a = item_a * 50
    price_b = item_b * 30
    price_c = item_c * 20
    price_d = item_d * 15

    discound_a = find_sku("AAA", skus)
    price_a -= 20 * discound_a

    discound_b = find_sku("BB", skus)
    price_b -= 15 * discound_b

    return price_a + price_b + price_c + price_d


