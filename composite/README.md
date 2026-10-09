# Composite Pattern

## What is Composite?

The Composite Pattern is a structural design pattern that allows individual objects and groups of objects to be treated uniformly.

## Before

In `before.py`, the `Folder` class can contain files, but it cannot contain other folders.

This limits the ability to represent nested folder structures.

## After

In `after.py`, both `File` and `Folder` implement the `FileSystemItem` abstraction.

- `File` represents an individual file.
- `Folder` represents a collection of file system items.
- `Folder` can contain both files and other folders.
- `show()` can be called on either a file or a folder.

This allows nested structures to be built and processed recursively.

## Pattern

> Compose objects into tree structures to represent part-whole hierarchies and treat individual objects and compositions uniformly.

## Technologies

- Python
- abc module
- Git
- GitHub
