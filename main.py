# Currency exchange profit calculator with manual table formatting

def print_table(rows):
    # Print header
    print(f"{'Profit (EGP)':>12} | {'Rate (EGP/USD)':>15}")
    print("-" * 30)
    # Print rows
    for profit, rate in rows:
        print(f"{profit:>12} | {rate:>15.4f}")

def main():
    print("Choose case type:")
    print("1 - Receiver gets EGP")
    print("2 - Receiver gets USD")
    case = int(input("Enter case type (1 or 2): "))

    R = float(input("Enter real exchange rate (EGP per USD): "))

    if case == 1:
        M = float(input("Enter fixed EGP amount: "))
        P = float(input("Enter desired profit in EGP: "))
        q = R / (1 + P / M)
        print(f"\nSet exchange rate to: {q:.4f} EGP/USD")

        rows = []
        for profit in [5, 10, 20, 50]:
            q_table = R / (1 + profit / M)
            rows.append((profit, q_table))

        print("\n--- Profit Table ---")
        print_table(rows)

    elif case == 2:
        U = float(input("Enter fixed USD amount: "))
        P = float(input("Enter desired profit in EGP: "))
        q = R + P / U
        print(f"\nSet exchange rate to: {q:.4f} EGP/USD")

        rows = []
        for profit in [5, 10, 20, 50]:
            q_table = R + profit / U
            rows.append((profit, q_table))

        print("\n--- Profit Table ---")
        print_table(rows)

    else:
        print("Invalid case type.")

if __name__ == "__main__":
    main()
