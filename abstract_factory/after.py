
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("Rendering Windows button")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering Windows checkbox")


class MacButton(Button):
    def render(self):
        print("Rendering Mac button")


class MacCheckbox(Checkbox):
    def render(self):
        print("Rendering Mac checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def create_ui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()


factory = WindowsFactory()
create_ui(factory)

print("---")

factory = MacFactory()
create_ui(factory)

