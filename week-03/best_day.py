import os

import my_tools

DATA_PATH = os.path.expanduser("~/de-bootcamp/ostad-de-bootcamp/module-02/data/raw_sales.txt")


def main():
    lines = my_tools.read_lines(DATA_PATH)

    d07 = 0
    d08 = 0
    d09 = 0
    d10 = 0
    d11 = 0

    for line in lines:
        parts = line.split(";")
        date = parts[1].strip()
        amount = my_tools.clean_amount(parts[5])
        status = my_tools.clean_text(parts[7])

        if status == "cancelled":
            continue

        if date == "2026-10-07":
            d07 += amount
        elif date == "2026-10-08":
            d08 += amount
        elif date == "2026-10-09":
            d09 += amount
        elif date == "2026-10-10":
            d10 += amount
        elif date == "2026-10-11":
            d11 += amount

    best_date = "2026-10-07"
    best_total = d07

    if d08 > best_total:
        best_date = "2026-10-08"
        best_total = d08
    if d09 > best_total:
        best_date = "2026-10-09"
        best_total = d09
    if d10 > best_total:
        best_date = "2026-10-10"
        best_total = d10
    if d11 > best_total:
        best_date = "2026-10-11"
        best_total = d11

    print("তারিখ ধরে হিসাব (বাতিল বাদে)")
    print()
    print("2026-10-07  ", my_tools.taka(d07))
    print("2026-10-08  ", my_tools.taka(d08))
    print("2026-10-09  ", my_tools.taka(d09))
    print("2026-10-10  ", my_tools.taka(d10))
    print("2026-10-11  ", my_tools.taka(d11))
    print()
    print("সবচেয়ে বেশি:", best_date, my_tools.taka(best_total))


if __name__ == "__main__":
    main()
