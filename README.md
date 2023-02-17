# Assignment
You are a bank account manager, and you have to calculate annual compound interest for 3 clients.

Write a program that asks each client what the principal amount is, what the time span is (in years), and what the interest rate is. Then print the compound interest for the user.

## Formulas
`A = P( 1 + R/100)^T`

`CI = A - P`

- A is Amount
- P is Principal Amount
- R is Interest Rate
- T is Time Span in Years
- CI is Compound Interest

## Starter Code
```python
# This first 3 lines are provided for you
client_one_principal = float(input("Principle (amount): "))
client_one_time =      float(input("Time:               "))
client_one_rate =      float(input("Rate:               "))
```

## Desired Output
```
Principle (amount): 1200
Time:               2
Rate:               5.4
Compound Interest:  133.1
---
Principle (amount): 12345
Time:               8
Rate:               6.7
Compound Interest:  8394.89
---
Principle (amount): 50
Time:               1
Rate:               1
Compound Interest:  0.5
```

## Testing
When you think your code if finished, run pytest in the terminal!
