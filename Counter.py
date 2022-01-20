from Hive import output_path
with open(output_path, "r") as f:
    amount = f.read().count(":")
    digits = len(str(amount))
    print(amount)
    print(digits)