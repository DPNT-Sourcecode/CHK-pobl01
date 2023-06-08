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

    total_price = 0

    if not set(skus).issubset(set(allowed_items.keys())):
        return -1

    for sku in allowed_items:
        item_count = find_sku(sku, skus)
        item_price = item_count * allowed_items[sku]

        if sku == "A":
            discount_count = item_count // 5

            if discount_count > 0:
                discound = 50 * discount_count
                item_price -= discount
                item_count -= discount_count * 5

            discount = 20 * (item_count // 3)
            item_price -= discount

        if sku == "B":
            discound = 15 * (item_count // 2)
            item_price -= discount

        if sku == "E" and "B" in skus:
            discound = allowed_items["B"] * (item_count // 2)
            item_price -= discount

        total_price += item_price
    return total_price
