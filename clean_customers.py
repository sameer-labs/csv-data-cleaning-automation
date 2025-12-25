import csv

input_file = "Raw_customers.csv"
output_file = "clean_customers.csv"

clean_rows = []
# Read raw CSV file
with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

# Clean malformed CSV rows
# Remove header quotes & split properly
header = rows[0][0].replace('"', '').split(',')

for r in rows[1:]:
    # Split the single quoted column
    values = r[0].replace('"', '').split(',')

    if len(values) != len(header):
        continue

    row = dict(zip(header, values))

    # Skip rows with missing Age
    if not row.get("Age"):
        continue

    clean_rows.append(row)

if not clean_rows:
    print("No valid rows found.")
else: # Write cleaned data to output file
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=clean_rows[0].keys())
        writer.writeheader()
        writer.writerows(clean_rows)

    print(f"Cleaned {len(clean_rows)} rows successfully.")

