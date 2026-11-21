import os

DATA_PATH = os.path.expanduser("~/de-bootcamp/ostad-de-bootcamp/module-02/data/raw_sales.txt")


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.readlines()


def clean_amount(text):
    return float(text.replace("৳", "").replace(",", "").strip())


def clean_text(text):
    return text.strip().lower()


def taka(amount):
    return f"৳{amount:.2f}"


def row(name, count, total):
    return f"{name:<18}{count}টা   {taka(total)}"


def main():
    lines = read_lines(DATA_PATH)

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
        amount = clean_amount(parts[5])
        payment = clean_text(parts[6])
        status = clean_text(parts[7])

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
    print(row("bkash", bkash_count, bkash_total))
    print(row("nagad", nagad_count, nagad_total))
    print(row("card", card_count, card_total))
    print(row("rocket", rocket_count, rocket_total))
    print(row("cash on delivery", cod_count, cod_total))
    print()
    print(f"সব মিলিয়ে: {taka(grand_total)}")


if __name__ == "__main__":
    main()
