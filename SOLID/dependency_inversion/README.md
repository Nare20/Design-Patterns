# Dependency Inversion Principle

## What is DIP?

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions.

## Before

In `before.py`, the `Notification` class directly creates an `EmailService` object.

This makes `Notification` dependent on a specific service. If we want to use SMS instead of email, we need to modify the `Notification` class.

This violates the Dependency Inversion Principle.

## After

In `after.py`, both `EmailService` and `SMSService` implement the `MessageService` abstraction.

The `Notification` class receives a service through its constructor instead of creating a specific service itself.

Now we can change the notification method without modifying the `Notification` class.

## Principle

> High-level and low-level modules should depend on abstractions, not on each other directly.

