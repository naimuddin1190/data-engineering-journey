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


if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))
    print(taka(1240.5))
