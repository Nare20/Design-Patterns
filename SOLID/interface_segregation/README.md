# Interface Segregation Principle

## What is ISP?

The Interface Segregation Principle states that a class should not be forced to depend on methods that it does not use.

## Before

In `before.py`, the `Worker` class contains both `work()` and `eat()` methods.

The `RobotWorker` class needs to work but does not need to eat. However, it inherits both methods and is forced to deal with a behavior it does not need.

This violates the Interface Segregation Principle.

## After

In `after.py`, the responsibilities are separated into smaller classes:

- `Workable` — defines the ability to work.
- `Eatable` — defines the ability to eat.
- `HumanWorker` — can work and eat.
- `RobotWorker` — can work without implementing an eating behavior.

Now each class depends only on the behaviors it needs.

## Principle

> Clients should not be forced to depend on methods they do not use.


