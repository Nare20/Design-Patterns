# Single Responsibility Principle

## What is SRP?

The Single Responsibility Principle states that a class should have one responsibility and one reason to change.

## Before

In `before.py`, the `Order` class has several responsibilities:

- Calculate the order total
- Save the order to the database
- Send a confirmation email
- Generate an invoice

This makes the class harder to maintain because changes in different parts of the application can affect the same class.

## After

In `after.py`, the responsibilities are separated:

- `Order` — stores order data and calculates the total
- `OrderRepository` — saves the order
- `EmailService` — sends confirmation emails
- `InvoiceGenerator` — generates invoices

Each class now has one main responsibility.

## Example

The program produces the same result before and after the refactoring, but the `after.py` version has a cleaner structure and follows SRP.

## Technologies

- Python
- Git
- GitHub
