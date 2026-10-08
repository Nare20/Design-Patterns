# Open/Closed Principle

## What is OCP?

The Open/Closed Principle states that a class should be open for extension but closed for modification.

This means that we should be able to add new functionality without changing existing, working code.

## Before

In `before.py`, the `Payment` class uses conditional statements to handle different payment methods.

For example:

- Card
- PayPal
- Cash

If we want to add a new payment method, such as Google Pay, we have to modify the `Payment` class.

This violates the Open/Closed Principle.

## After

In `after.py`, each payment method is implemented as a separate class.

- `CardPayment` — handles card payments
- `PayPalPayment` — handles PayPal payments
- `CashPayment` — handles cash payments
- `Payment` — processes the selected payment method

If we want to add a new payment method, we can create a new class without modifying the existing `Payment` class.

For example:

```python
class GooglePayPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} with Google Pay")
```

This allows the system to be extended without modifying existing code.

## Before vs After

### Before

Adding a new payment method requires modifying the existing `Payment` class.

### After

Adding a new payment method only requires creating a new class.

## Principle

> A class should be open for extension but closed for modification.
