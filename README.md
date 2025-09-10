# FX Profit Calculator

A simple Python tool to calculate custom FX (Foreign Exchange) rates with profit margins.  
It helps you set exchange rates when converting between USD and EGP, ensuring you add your desired profit.

## Features
- Two modes:
  - Receiver gets EGP (you deduct USD).
  - Receiver gets USD (they pay in EGP).
- Calculates the exact exchange rate required to achieve a given profit.
- Generates a quick profit table for multiple scenarios.

## How it works
- Enter the real exchange rate (e.g., 48 EGP/USD).
- Choose the case type:
  - Case 1: Receiver gets EGP → You deduct USD.
  - Case 2: Receiver gets USD → They pay EGP.
- Enter the fixed amount and your desired profit.
- The tool prints the adjusted exchange rate and a profit table.

## Example Usage
```bash
$ python main.py
Choose case type:
1 - Receiver gets EGP
2 - Receiver gets USD
Enter case type (1 or 2): 1
Enter real exchange rate (EGP per USD): 48
Enter fixed EGP amount: 500
Enter desired profit in EGP: 10

Set exchange rate to: 47.0588 EGP/USD

--- Profit Table ---
Profit (EGP) |  Rate (EGP/USD)
------------------------------
           5 |         47.5248
          10 |         47.0588
          20 |         46.1538
          50 |         43.6364
