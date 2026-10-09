# Singleton Pattern

## What is Singleton?

The Singleton Pattern ensures that a class has only one instance and provides a single point of access to that instance.

## Before

In `before.py`, every call to `GameSettings()` creates a new object.

Changing the volume of one object does not affect the other object.

Therefore, `settings1` and `settings2` are different instances.

## After

In `after.py`, the `__new__()` method controls object creation.

The first call creates an instance and stores it in `_instance`. Later calls return the same instance.

As a result, `settings1` and `settings2` refer to the same object, and changes to its volume are visible through both variables.

## Pattern

> Ensure that a class has only one instance and provide a global point of access to it.

