""" calculate the tip based on the bill amount and tip percentage """

def main():
    dollars = dollars_to_float(input("Enter the bill amount: $"))
    percent = percent_to_float(input("Enter the tip percentage: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d: str) -> float:
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p: str) -> float:
    p = p.replace("%", "")
    return float(p) / 100.0

main()