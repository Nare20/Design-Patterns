# Liskov Substitution Principle

## What is LSP?

The Liskov Substitution Principle states that objects of a subclass should be able to replace objects of their parent class without breaking the program.

## Before

In `before.py`, `Penguin` inherits from `Bird`, but it cannot perform the `fly()` behavior defined by `Bird`.

When `make_bird_fly()` receives a `Penguin`, the program raises an exception.

This violates the Liskov Substitution Principle.

## After

In `after.py`, the `Bird` class contains common behavior, while flying birds are represented by `FlyingBird`.

- `Bird` — common bird behavior
- `FlyingBird` — behavior for birds that can fly
- `Sparrow` — a flying bird
- `Penguin` — a bird that can swim

Now `Penguin` is not forced to implement a behavior it cannot perform.

## Principle

> Subclasses should be replaceable for their parent classes without changing the correctness of the program.

