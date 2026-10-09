# Abstract Factory Pattern

## What is Abstract Factory?

The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related objects without specifying their concrete classes.

## Before

In `before.py`, the client code uses conditional statements to create platform-specific buttons and checkboxes.

As more platforms are added, the client code becomes more complicated.

## After

In `after.py`, the `GUIFactory` abstraction defines methods for creating buttons and checkboxes.

- `WindowsFactory` creates Windows UI components.
- `MacFactory` creates Mac UI components.
- `Button` and `Checkbox` define common interfaces for the products.
- `create_ui()` uses the factory without depending on a specific platform.

Each factory creates a consistent family of related UI components.

## Pattern

> Create families of related objects without specifying their concrete classes.

## Technologies

- Python
- abc module
- Git
- GitHub
