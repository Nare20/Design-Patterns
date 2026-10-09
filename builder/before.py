
class Computer:
    def __init__(self, cpu, ram, storage, graphics_card):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card

    def show_specs(self):
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print(f"Graphics Card: {self.graphics_card}")


computer = Computer(
    "Intel Core i7",
    "16GB",
    "1TB SSD",
    "NVIDIA RTX 4060"
)

computer.show_specs()

