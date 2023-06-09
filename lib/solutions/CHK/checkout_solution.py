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

    discount_thresholds = {"two": 2,
                           "three": 3,
                           "five": 5,
                           "ten": 10}
                        #{"fiveAs": 5,
                          # "threeAs": 3,
                          # "twoBs": 2,
                          # "twoEs": 2,
                          # "threeFs": 3,
                          # "fiveHs": 5,
                          # "tenHs": 10,
                          # "twoKs": 2,
                          # "threeNs": 3,
                          # "fivePs": 5}

    discount_rates = {"fiveAs": 50,
                      "threeAs": 20,
                      "twoBs": 15,
                      "twoEs": sku_price_table["B"],
                      "threeFs": sku_price_table["F"],
                      "tenHs": 20,
                      "fiveHs": 5,
                      "twoKs": 10,
                      "threeNs": sku_price_table["M"],
                      "fivePs": 50,
                      "threeRs": sku_price_table["Q"],
                      "threeQs": 10,
                      "threeUs": sku_price_table["U"],
                      "threeVs": 20,
                      "twoVs": 10}
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
        disc_freq_five_a = calculate_discount_frequency(sku_count["A"], discount_thresholds["five"])
        discount_five_a = calculate_discount(disc_freq_five_a, discount_rate["fiveAs"])
        sku_prices["A"] -= discount_five_a

        remaining_a = sku_count["A"] - disc_freq_five_a * discount_thresholds["five"]
        sku_prices["A"] -= calculate_discount_quick(remaining_a, discount_thresholds["three"], discount_rate["threeAs"])

    if "E" in sku_count and "B" in sku_count:
        disc_freq_two_e = calculate_discount_frequency(sku_count["E"], discount_thresholds["two"])
        discount_two_e = calculate_discount(disc_freq_two_e, discount_rate["twoEs"])
        sku_prices["B"] -= discount_two_e

        if sku_prices["B"] < 0:
            sku_prices["B"] = 0
        sku_count["B"] -= disc_freq_two_e

    if "B" in sku_count:
        sku_prices["B"] -= calculate_discount_quick(sku_count["B"], discount_thresholds["two"], discount_rate["twoBs"])

    if "F" in sku_count:
        sku_prices["F"] -= calculate_discount_quick(sku_count["F"], discount_thresholds["three"], discount_rate["threeFs"])

    if "H" in sku_count:
        disc_freq_ten_h = calculate_discount_frequency(sku_count["H"], discount_thresholds["ten"])
        discount_ten_h = calculate_discount(disc_freq_ten_h, discount_rate["tenHs"])
        sku_prices["H"] -= discount_ten_h

        remaining_h = sku_count["H"] - disc_freq_ten_h * discount_thresholds["ten"]
        sku_prices["H"] -= calculate_discount_quick(remaining_h, discount_thresholds["five"], discount_rate["fiveHs"])

    if "K" in sku_count:
        sku_prices["K"] -= calculate_discount_quick(sku_count["K"], discount_thresholds["two"], discount_rate["twoKs"])

    if "N" in sku_count:
        sku_prices["M"] -= calculate_discount_quick(sku_count["N"], discount_thresholds["three"], discount_rate["threeNs"])

    if "P" in sku_count:
        sku_prices["P"] -= calculate_discount_quick(sku_count["P"], discount_thresholds["five"], discount_rate["fivePs"])

    if "R" in sku_count and "Q" in sku_count:
        disc_freq_three_r = calculate_discount_frequency(sku_count["R"], discount_thresholds["three"])
        discount_three_r = calculate_discount(disc_freq_three_r, discount_rate["threeRs"])
        sku_prices["Q"] -= discount_three_r

        if sku_prices["Q"] < 0:
            sku_prices["Q"] = 0
        sku_count["Q"] -= disc_freq_three_r

    if "Q" in sku_count:
        sku_prices["Q"] -= calculate_discount_quick(sku_count["Q"], discount_thresholds["three"], discount_rate["threeQs"])

    if "U" in sku_count:
        sku_prices["U"] -= calculate_discount_quick(sku_count["U"], discount_thresholds["three"], discount_rate["threeUs"])

    if "V" in sku_count:
        disc_freq_three_v = calculate_discount_frequency(sku_count["V"], discount_thresholds["three"])
        discount_three_v = calculate_discount(disc_freq_three_v, discount_rate["threeVs"])
        sku_prices["V"] -= discount_three_v

        remaining_v = sku_count["V"] - disc_freq_three_v * discount_thresholds["three"]
        sku_prices["V"] -= calculate_discount_quick(remaining_v, discount_thresholds["two"], discount_rate["twoVs"])

    total_price = sum(sku_prices.values())

    return total_price








