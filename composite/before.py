
class File:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"File: {self.name}")


class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def show(self):
        print(f"Folder: {self.name}")

        for file in self.files:
            file.show()


file1 = File("notes.txt")
file2 = File("photo.png")

folder = Folder("Documents")
folder.add_file(file1)
folder.add_file(file2)

folder.show()

