import re

def find_sku(sku, skus):
    return len(list(re.finditer(sku, skus)))

def calculate_discount_frequency(sku_count, discount_threshold):
    return sku_count // discount_threshold

def calculate_discount(discount_freq, discount_rate):
    return discount_freq * discount_rate

def calculate_discount_quick(sku_count, discount_threshold, discount_rate):
    disc_freq = calculate_drscount_frequency(sku_count, discount_threshold)
    return calculate_discount(disc_freq, discount_rate)

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
                       "E": 40,
                       "F": 10,
                       "G": 20,
                       "H": 10,
                       "I": 35,
                       "J": 60,
                       "K": 80,
                       "L": 90,
                       "M": 15,
                       "N": 40,
                       "O": 10,
                       "P": 50,
                       "Q": 30,
                       "R": 50,
                       "S": 30,
                       "T": 20,
                       "U": 40,
                       "V": 50,
                       "W": 20,
                       "X": 90,
                       "Y": 10,
                       "Z": 50}

    discount_thresholds = {"fiveAs": 5, "threeAs": 3, "twoBs": 2, "twoEs": 2, "threeFs": 3}
    discount_rates = {"fiveAs": 50, "threeAs": 20, "twoBs": 15, "twoEs": sku_price_table["B"], "threeFs": sku_price_table["F"]}
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
	disc_freq_five_a = calculate_discount_frequency(sku_count["A"], discount_thresholds["fiveAs"])
	discount_five_a = calculate_discount(disc_freq_five_a, discount_rate["fiveAs"])
	sku_prices["A"] -= discount_five_a

        remaining_a = sku_count["A"] - disc_freq_five_a * discount_thresholds["fiveAs"]
	sku_prices["A"] -= calculate_discount_quick(remaining_a, discount_thresholds["threeAs"], discount_rate["threeAs"])

    if "E" in sku_count and "B" in sku_count:
	disc_freq_two_e = calculate_discount_frequency(sku_count["E"], discount_thresholds["twoEs"])
	discount_two_e = calculate_discount(disc_freq_two_e, discount_rate["twoEs"])
        sku_prices["B"] -= discount_two_e
        #discount_two_e = sku_count["E"] // discount_thresholds["twoEs"]  #TODO
        #sku_prices["B"] -= discount_rates["twoEs"] * discount_two_e
        if sku_prices["B"] < 0:
            sku_prices["B"] = 0
        sku_count["B"] -= disc_freq_two_e

    if "B" in sku_count:
        sku_prices["B"] -= calculate_discount(sku_count["B"], discount_thresholds["twoBs"], discount_rates["twoBs"])
        #discount_two_b = sku_count["B"] // discount_thresholds["twoBs"]
        #sku_prices["B"] -= discount_rates["twoBs"] * discount_two_b

    if "F" in sku_count:
        sku_prices["F"] -= calculate_discount(sku_count["F"], discount_thresholds["threeFs"], discount_rates["threeFs"])
        #discount_two_f = sku_count["F"] // discount_thresholds["threeFs"]
        #sku_prices["F"] -= discount_rates["threeFs"] * discount_two_f

    total_price = sum(sku_prices.values())

    return total_price






