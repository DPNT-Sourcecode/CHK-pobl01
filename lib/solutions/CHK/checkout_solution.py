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
    #print(sku_count)

    for sku in sku_count:
        sku_prices[sku] = sku_count[sku] * sku_price_table[sku]
        total_price += sku_prices[sku]
    #print(sku_prices)

    if "A" in sku_count:
        discount_five_a = sku_count["A"] // discount_thresholds["fiveAs"]
        sku_prices["A"] -= discount_rates["fiveAs"] * discount_five_a
        #sku_count["A"] -= discount_five_a

        remaining_a = sku_count["A"] - discount_five_a * discount_thresholds["fiveAs"]
        discount_three_a = remaining_a // discount_thresholds["threeAs"]
        sku_prices["A"] -= discount_rates["threeAs"] * discount_three_a
        #sku_count["A"] -= discount_three_a

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

    #calculate_discount()
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

out = checkout("")
print(out)
out = checkout("A")
print(out)
out = checkout("B")
print(out)
out = checkout("C")
print(out)
out = checkout("D")
print(out)
out = checkout("E")
print(out)
out = checkout("a")
print(out)
out = checkout("-")
print(out)
out = checkout("ABCa")
print(out)
out = checkout("AxA")
print(out)
out = checkout("ABCDE")
print(out)
out = checkout("A")
print(out)
out = checkout("AA")
print(out)
out = checkout("AAA")
print(out)
out = checkout("AAAA")
print(out)
out = checkout("AAAAA")
print(out)
out = checkout("AAAAAA")
print(out)
out = checkout("AAAAAAA")
print(out)
out = checkout("AAAAAAAA")
print(out)
out = checkout("AAAAAAAAA")
print(out)
out = checkout("AAAAAAAAAA")
print(out)
out = checkout("EE")
print(out)
out = checkout("EEB")
print(out)
out = checkout("EEEB")
print(out)
out = checkout("EEEEBB")
print(out)
out = checkout("BEBEEE")
print(out)
out = checkout("A")
print(out)
out = checkout("AA")
print(out)
out = checkout("AAA")
print(out)
out = checkout("AAAA")
print(out)
out = checkout("AAAAA")
print(out)
out = checkout("AAAAAA")
print(out)
out = checkout("B")
print(out)
out = checkout("BB")
print(out)
out = checkout("BBB")
print(out)
out = checkout("BBBB")
print(out)
out = checkout("ABCDEABCDE")
print(out)
out = checkout("CCADDEEBBA")
print(out)
out = checkout("AAAAAEEBAAABB")
print(out)
out = checkout("ABCDECBAABCABBAAAEEAA")
print(out)
