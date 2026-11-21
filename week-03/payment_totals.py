import os

path = os.path.expanduser("~/de-bootcamp/ostad-de-bootcamp/module-02/data/raw_sales.txt")

with open(path, encoding="utf-8") as f:
    lines = f.readlines()

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
    amount_text = parts[5].replace("৳", "").replace(",", "").strip()
    amount = float(amount_text)
    payment = parts[6].strip().lower()
    status = parts[7].strip().lower()

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
print(f"{'bkash':<18}{bkash_count}টা   ৳{bkash_total:.2f}")
print(f"{'nagad':<18}{nagad_count}টা   ৳{nagad_total:.2f}")
print(f"{'card':<18}{card_count}টা   ৳{card_total:.2f}")
print(f"{'rocket':<18}{rocket_count}টা   ৳{rocket_total:.2f}")
print(f"{'cash on delivery':<18}{cod_count}টা   ৳{cod_total:.2f}")
print()
print(f"সব মিলিয়ে: ৳{grand_total:.2f}")
