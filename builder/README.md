# Builder Pattern

## What is Builder?

The Builder Pattern is a creational design pattern that allows a complex object to be constructed step by step.

It separates the construction process from the final object.

## Before

In `before.py`, the `Computer` object is created by passing all its parameters to the constructor.

As the number of parameters grows, object creation can become difficult to read and maintain.

## After

In `after.py`, the `ComputerBuilder` class constructs the computer step by step.

- `set_cpu()` configures the processor.
- `set_ram()` configures the memory.
- `set_storage()` configures the storage.
- `set_graphics_card()` configures the graphics card.
- `build()` returns the completed computer.

Each configuration method returns the builder itself, allowing method chaining.

## Pattern

> Separate the construction of a complex object from its representation, allowing the same construction process to create different representations.
