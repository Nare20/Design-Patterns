
from abc import ABC, abstractmethod


class FileSystemItem(ABC):
    @abstractmethod
    def show(self):
        pass


class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"File: {self.name}")


class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print(f"Folder: {self.name}")

        for item in self.items:
            item.show()


file1 = File("notes.txt")
file2 = File("photo.png")

subfolder = Folder("Images")
subfolder.add(file2)

main_folder = Folder("Documents")
main_folder.add(file1)
main_folder.add(subfolder)

main_folder.show()

