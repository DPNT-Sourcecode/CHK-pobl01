import re

def calculate_discount_frequency(sku_count, discount_threshold):
    return sku_count // discount_threshold

def calculate_discount(discount_freq, discount_rate):
    return discount_freq * discount_rate

def calculate_discount_quick(sku_count, discount_threshold, discount_rate):
    disc_freq = calculate_discount_frequency(sku_count, discount_threshold)
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

    sku_price_table = { "A": 50,
                        "B": 30,
                        "C": 20,
                        "D": 15,
                        "E": 40,
                        "F": 10,
                        "G": 20,
                        "H": 10,
                        "I": 35,
                        "J": 60,
                        "K": 70,
                        "L": 90,
                        "M": 15,
                        "N": 40,
                        "O": 10,
                        "P": 50,
                        "Q": 30,
                        "R": 50,
                        "S": 20,
                        "T": 20,
                        "U": 40,
                        "V": 50,
                        "W": 20,
                        "X": 17,
                        "Y": 20,
                        "Z": 21}

    discount_thresholds = {"two": 2,
                           "three": 3,
                           "four": 4,
                           "five": 5,
                           "ten": 10}

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

    any_three_discount = ["Z", "S", "T", "Y", "X"]  # Sorted by price in descending order

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
        discount_five_a = calculate_discount(disc_freq_five_a, discount_rates["fiveAs"])
        sku_prices["A"] -= discount_five_a

        remaining_a = sku_count["A"] - disc_freq_five_a * discount_thresholds["five"]
        sku_prices["A"] -= calculate_discount_quick(remaining_a, discount_thresholds["three"], discount_rates["threeAs"])

    if "E" in sku_count and "B" in sku_count:
        disc_freq_two_e = calculate_discount_frequency(sku_count["E"], discount_thresholds["two"])
        discount_two_e = calculate_discount(disc_freq_two_e, discount_rates["twoEs"])
        sku_prices["B"] -= discount_two_e

        if sku_prices["B"] < 0:
            sku_prices["B"] = 0
        sku_count["B"] -= disc_freq_two_e

    if "B" in sku_count:
        sku_prices["B"] -= calculate_discount_quick(sku_count["B"], discount_thresholds["two"], discount_rates["twoBs"])

    if "F" in sku_count:
        sku_prices["F"] -= calculate_discount_quick(sku_count["F"], discount_thresholds["three"], discount_rates["threeFs"])

    if "H" in sku_count:
        disc_freq_ten_h = calculate_discount_frequency(sku_count["H"], discount_thresholds["ten"])
        discount_ten_h = calculate_discount(disc_freq_ten_h, discount_rates["tenHs"])
        sku_prices["H"] -= discount_ten_h

        remaining_h = sku_count["H"] - disc_freq_ten_h * discount_thresholds["ten"]
        sku_prices["H"] -= calculate_discount_quick(remaining_h, discount_thresholds["five"], discount_rates["fiveHs"])

    if "K" in sku_count:
        sku_prices["K"] -= calculate_discount_quick(sku_count["K"], discount_thresholds["two"], discount_rates["twoKs"])

    if "N" in sku_count and "M" in sku_count:
        disc_freq_three_n = calculate_discount_frequency(sku_count["N"], discount_thresholds["three"])
        discount_three_n = calculate_discount(disc_freq_three_n, discount_rates["threeNs"])
        sku_prices["M"] -= discount_three_n

        if sku_prices["M"] < 0:
            sku_prices["M"] = 0
        sku_count["M"] -= disc_freq_three_n

    if "P" in sku_count:
        sku_prices["P"] -= calculate_discount_quick(sku_count["P"], discount_thresholds["five"], discount_rates["fivePs"])

    if "R" in sku_count and "Q" in sku_count:
        disc_freq_three_r = calculate_discount_frequency(sku_count["R"], discount_thresholds["three"])
        discount_three_r = calculate_discount(disc_freq_three_r, discount_rates["threeRs"])
        sku_prices["Q"] -= discount_three_r

        if sku_prices["Q"] < 0:
            sku_prices["Q"] = 0
        sku_count["Q"] -= disc_freq_three_r

    if "Q" in sku_count:
        sku_prices["Q"] -= calculate_discount_quick(sku_count["Q"], discount_thresholds["three"], discount_rates["threeQs"])

    if "U" in sku_count:
        sku_prices["U"] -= calculate_discount_quick(sku_count["U"], discount_thresholds["four"], discount_rates["threeUs"])

    if "V" in sku_count:
        disc_freq_three_v = calculate_discount_frequency(sku_count["V"], discount_thresholds["three"])
        discount_three_v = calculate_discount(disc_freq_three_v, discount_rates["threeVs"])
        sku_prices["V"] -= discount_three_v

        remaining_v = sku_count["V"] - disc_freq_three_v * discount_thresholds["three"]
        sku_prices["V"] -= calculate_discount_quick(remaining_v, discount_thresholds["two"], discount_rates["twoVs"])

    #if any([sku in any_three_discount for sku in sku_count]):
    # find skus to be checked for discount
    any_three_discount_skus = {}
    for sku in sku_count:
        if sku in any_three_discount:
             any_three_discount_skus[sku] = sku_count[sku]
    if any_three_discount_skus:
        total_disc_skus = 3
        any_three_disc_rate = 45
        # how many times will the discount be applied? 
        any_three_discount_freq = sum(any_three_discount_skus.values()) // total_disc_skus
        # for each discount remove items that dont get a discount
        for _ in range(any_three_discount_freq):
            breakpoint()
            for sku in any_three_discount:
                left_to_remove = total_disc_skus - any_three_discount_skus[sku]
                if left_to_remove < 0:
                    any_three_discount_skus[sku] -= total_disc_skus
                else:
                    any_three_discount_skus[sku] -= (total_disc_skus-left_to_remove)
        temp_price = sum([any_three_discount_skus[sku] * sku_price_table[sku] for sku in any_three_discount_skus])
        any_three_discount_price = sum(sku_prices.values()) - temp_price

        print(sku_prices)
        print(any_three_discount_skus)
        total_price = sum(sku_prices.values())
        total_price -= any_three_discount_price
        total_price += any_three_disc_rate * any_three_discount_freq
    else:
        total_price = sum(sku_prices.values())

    return total_price

out = checkout("STXYZ")
print(out)








