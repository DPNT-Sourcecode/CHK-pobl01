import re

def find_sku(sku, skus):
    return len(list(re.finditer(sku, skus)))

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    allowed_items = {"A": 50,
                     "B": 30,
                     "C": 20,
                     "D": 15,
                     "E": 40}

    if not set(skus).issubset(set(allowed_items.keys())):
        return -1

    for sku in allowed_items:
        item_count = find_sku(sku, skus)
        item_price = item_count * allowed_items[sku]

        if sku == "A":
            discount_count = item_count // 5
            if discount_count:

    discound_a = 20 * (item_a // 3)
    price_a -= discound_a

    discound_b = 15 * (item_b // 2)
    price_b -= discound_b

    return price_a + price_b + price_c + price_d

