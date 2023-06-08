import re

def find_sku(sku, skus):
    return len(list(re.finditer(sku, skus)))

def calculate_discount(discount, sku_count, discount_threshold):
    return discount * (sku_count // discount_threshold)

def count_skus(skus):
    unique_skus = set(skus)
    res = {}
    for sku in skus:
        res[sku] = skus.count(sku)
    return res

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    sku_price_table = {"A": 50,
                       "B": 30,
                       "C": 20,
                       "D": 15,
                       "E": 40}

    discount_thresholds = {"fiveAs": 5, "threeAs": 3, "twoBs": 2, "twoEs": 2}
    sku_prices = {}

    total_price = 0

    # Check for invalid characters.
    if not set(skus).issubset(set(sku_price_table.keys())):
        return -1

    sku_count = count_skus(skus)
    print(sku_count)

    for sku in sku_count:
        sku_prices[sku] = sku_count[sku] * sku_price_table[sku]
        total_price += sku_prices[sku]
    print(sku_prices)

    discount_a = sku_count["A"] // discount_a_threshold
    calculate_discount()
    #for sku in allowed_items:
    #    item_count = find_sku(sku, skus)
    #    item_price = item_count * allowed_items[sku]
    #    print(f"item price {sku}",item_price)

    #    if sku == "A":
    #        discount_count = item_count // 5

    #        if discount_count > 0:
    #            discount = 50 * discount_count
    #            item_price -= discount
    #            item_count -= discount_count * 5

    #        discount = 20 * (item_count // 3)
    #        item_price -= discount

    #    if sku == "B":
    #        discount = 15 * (item_count // 2)
    #        item_price -= discount

    #    if sku == "E" and "B" in skus:
    #        discount = allowed_items["B"] * (item_count // 2)
    #        #print("discount",discount)
    #        #print("item price",item_price)
    #        item_price -= discount
    #        #print("item price",item_price)

    #    total_price += item_price
    return total_price

out = checkout("EEEEBB")
print(out)


