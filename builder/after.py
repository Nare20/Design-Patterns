
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None

    def show_specs(self):
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print(f"Graphics Card: {self.graphics_card}")


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer


computer = (
    ComputerBuilder()
    .set_cpu("Intel Core i7")
    .set_ram("16GB")
    .set_storage("1TB SSD")
    .set_graphics_card("NVIDIA RTX 4060")
    .build()
)

computer.show_specs()

