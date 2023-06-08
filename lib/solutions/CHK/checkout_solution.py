import re

def find_sku(sku, skus):
    return len(list(re.finditer(sku, skus)))

def calculate_discount(discount, sku_count, discount_threshold):
    return discount * (sku_count // discount_threshold)

def count_skus(skus):
    unique_skus = set(skus)
    res = {}
    for sku in unique_skus:
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
    discount_rates = {"fiveAs": 50, "threeAs": 20, "twoBs": 15, "twoEs": sku_price_table["B"]}
    sku_prices = {}

    total_price = 0

    # Check for invalid characters.
    if not set(skus).issubset(set(sku_price_table.keys())):
        return -1

    sku_count = count_skus(skus)

    for sku in sku_count:
        sku_prices[sku] = sku_count[sku] * sku_price_table[sku]
        total_price += sku_prices[sku]

    if "A" in sku_count:
        discount_five_a = sku_count["A"] // discount_thresholds["fiveAs"]
        sku_prices["A"] -= discount_rates["fiveAs"] * discount_five_a

        remaining_a = sku_count["A"] - discount_five_a * discount_thresholds["fiveAs"]
        discount_three_a = remaining_a // discount_thresholds["threeAs"]
        sku_prices["A"] -= discount_rates["threeAs"] * discount_three_a

    if "E" in sku_count and "B" in sku_count:
        discount_two_e = sku_count["E"] // discount_thresholds["twoEs"]
        sku_prices["B"] -= discount_rates["twoEs"] * discount_two_e
        if sku_prices["B"] < 0:
            sku_prices["B"] = 0
        sku_count["B"] -= discount_two_e

    if "B" in sku_count:
        discount_two_b = sku_count["B"] // discount_thresholds["twoBs"]
        sku_prices["B"] -= discount_rates["twoBs"] * discount_two_b

    total_price = sum(sku_prices.values())

    return total_price

