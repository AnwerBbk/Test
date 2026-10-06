import csv

def extract_sales(filepath):
    sales = []

    with open(filepath, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for line_no, row in enumerate(reader, start=2):
            try:
                row["amount"] = float(row["quantity"]) * float(row["unit_price"])
            except (ValueError, KeyError) as e:
                print(f"Ligne {line_no} ignorée: {e}")
                continue
            sales.append(row)

    return sales

data = extract_sales("sales.csv")

for s in data[:3]:
    print(s["product"], s["amount"])