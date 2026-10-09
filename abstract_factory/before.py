
class WindowsButton:
    def render(self):
        print("Rendering Windows button")


class WindowsCheckbox:
    def render(self):
        print("Rendering Windows checkbox")


class MacButton:
    def render(self):
        print("Rendering Mac button")


class MacCheckbox:
    def render(self):
        print("Rendering Mac checkbox")


os_type = "windows"

if os_type == "windows":
    button = WindowsButton()
    checkbox = WindowsCheckbox()
elif os_type == "mac":
    button = MacButton()
    checkbox = MacCheckbox()
else:
    raise ValueError("Unknown operating system")

button.render()
checkbox.render()

