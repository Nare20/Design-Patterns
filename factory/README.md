# Factory Pattern

## What is Factory?

The Factory Pattern is a creational design pattern that encapsulates object creation in a separate method or class.

It allows the client code to request an object without directly creating a specific class instance.

## Before

In `before.py`, the client code uses conditional statements to decide which notification object to create.

As new notification types are added, the object creation logic can become harder to maintain.

## After

In `after.py`, the `NotificationFactory` class handles the creation of notification objects.

- `EmailNotification` sends email notifications.
- `SMSNotification` sends SMS notifications.
- `NotificationFactory` creates the requested notification object.

The client code requests an object from the factory and then uses its `send()` method.

## Pattern

> Encapsulate object creation so that client code does not need to create concrete objects directly.

## Technologies

- Python
- Git
- GitHub
