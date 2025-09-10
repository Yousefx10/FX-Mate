# Currency exchange profit calculator with profit table

def main():
    print("Choose case type:")
    print("1 - Receiver gets EGP")
    print("2 - Receiver gets USD")
    case = int(input("Enter case type (1 or 2): "))

    R = float(input("Enter real exchange rate (EGP per USD): "))

    if case == 1:
        # Case 1: Receiver gets EGP, so you deduct USD
        M = float(input("Enter fixed EGP amount: "))
        P = float(input("Enter desired profit in EGP: "))
        q = R / (1 + P / M)
        print(f"\nSet exchange rate to: {q:.4f} EGP/USD")

        # Extra table for different profit values
        print("\n--- Profit Table ---")
        for profit in [5, 10, 20, 50]:
            q_table = R / (1 + profit / M)
            print(f"Profit {profit:>3} EGP -> Rate: {q_table:.4f}")

    elif case == 2:
        # Case 2: Receiver gets USD, so they pay EGP
        U = float(input("Enter fixed USD amount: "))
        P = float(input("Enter desired profit in EGP: "))
        q = R + P / U
        print(f"\nSet exchange rate to: {q:.4f} EGP/USD")

        # Extra table for different profit values
        print("\n--- Profit Table ---")
        for profit in [5, 10, 20, 50]:
            q_table = R + profit / U
            print(f"Profit {profit:>3} EGP -> Rate: {q_table:.4f}")

    else:
        print("Invalid case type.")

if __name__ == "__main__":
    main()
