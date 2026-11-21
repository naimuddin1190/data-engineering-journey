import os

import my_tools

DATA_PATH = os.path.expanduser("~/de-bootcamp/ostad-de-bootcamp/module-02/data/raw_sales.txt")


def main():
    lines = my_tools.read_lines(DATA_PATH)

    bkash_count = 0
    bkash_total = 0
    nagad_count = 0
    nagad_total = 0
    card_count = 0
    card_total = 0
    rocket_count = 0
    rocket_total = 0
    cod_count = 0
    cod_total = 0

    for line in lines:
        parts = line.split(";")
        amount = my_tools.clean_amount(parts[5])
        payment = my_tools.clean_text(parts[6])
        status = my_tools.clean_text(parts[7])

        if status == "cancelled":
            continue

        if payment == "bkash":
            bkash_count += 1
            bkash_total += amount
        elif payment == "nagad":
            nagad_count += 1
            nagad_total += amount
        elif payment == "card":
            card_count += 1
            card_total += amount
        elif payment == "rocket":
            rocket_count += 1
            rocket_total += amount
        elif payment == "cash on delivery":
            cod_count += 1
            cod_total += amount

    grand_total = bkash_total + nagad_total + card_total + rocket_total + cod_total

    print("payment ধরে হিসাব (বাতিল বাদে)")
    print()
    print(my_tools.row("bkash", bkash_count, bkash_total))
    print(my_tools.row("nagad", nagad_count, nagad_total))
    print(my_tools.row("card", card_count, card_total))
    print(my_tools.row("rocket", rocket_count, rocket_total))
    print(my_tools.row("cash on delivery", cod_count, cod_total))
    print()
    print(f"সব মিলিয়ে: {my_tools.taka(grand_total)}")


if __name__ == "__main__":
    main()
