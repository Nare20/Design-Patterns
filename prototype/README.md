# Prototype Pattern

## What is Prototype?

The Prototype Pattern is a creational design pattern that creates new objects by copying existing objects instead of constructing them from scratch.

## Before

In `before.py`, a new `GameCharacter` object is created by manually passing the properties of an existing character to the constructor.

This can become inconvenient when an object has many properties.

## After

In `after.py`, the `GameCharacter` class provides a `clone()` method that creates a copy of the existing object using `copy.deepcopy()`.

The copied character can be modified independently of the original character.

## Pattern

> Create new objects by copying existing instances, rather than creating them from scratch.

## Technologies

- Python
- copy module
- Git
- GitHub
