import copy


class ComputerStore:
    def __init__(self):
        self.computers = []

    def add_computer(self, computer):
        self.computers.append(computer)

    def display_computers(self):
        for i, computer in enumerate(self.computers):
            print(f"Computer {i + 1}:")
            print(f"Case: {computer.case}")
            print(f"Motherboard: {computer.motherboard}")
            print(f"CPU: {computer.cpu}")
            print(f"Memory: {computer.memory}")
            print(f"Storage: {computer.storage}")
            print(f"GPU: {computer.gpu}")
            print(f"Price: {computer.price}")
            print()


class Computer:

    def __init__(self, case, motherboard, cpu, memory, storage, gpu, price, additional_components=None):
        self.case = case
        self.motherboard = motherboard
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.gpu = gpu
        self.price = price
        self.additional_components = additional_components if additional_components else []

    def clone(self):
        return Computer(
            self.case,
            self.motherboard,
            self.cpu,
            self.memory,
            self.storage,
            self.gpu,
            self.price,
            additional_components=copy.deepcopy(self.additional_components)
        )


if __name__ == '__main__':
    base_computer = Computer(
        "Basic Case",
        "Standard Motherboard",
        "Intel Core i5",
        "8GB RAM",
        "256GB SSD",
        "NVIDIA",
        800,
        additional_components=["Keyboard", "Mouse", "Monitor"]
    )

    computer_store = ComputerStore()
    computer_store.add_computer(base_computer)

    # tezi nacin
    # computer_store.add_computer(
    #     Computer("Basic Case", "Standard Motherboard", "AMD Ryzen 7", "8GB RAM", "256GB SSD", "NVIDIA", 800,
    #              additional_components=["Keyboard", "Mouse", "Monitor"]))
    # computer_store.add_computer(
    #     Computer("Basic Case", "Standard Motherboard", "AMD Ryzen 7", "32GB RAM", "256GB SSD", "NVIDIA", 800,
    #              additional_components=["Keyboard", "Mouse", "Monitor"]))

    comp1 = base_computer.clone()
    comp1.cpu = "AMD Ryzen 7"
    computer_store.add_computer(comp1)

    comp2 = comp1.clone()
    comp2.memory = "32GB RAM"
    computer_store.add_computer(comp2)

    comp3 = comp2.clone()
    comp3.gpu = "AMD Radeon RX 6900 XT"
    computer_store.add_computer(comp3)

    comp4 = comp3.clone()
    comp4.gpu = "NVIDIA GTX 1660"
    computer_store.add_computer(comp4)

    comp5 = comp4.clone()
    comp5.gpu = "AMD Radeon RX 570"
    computer_store.add_computer(comp5)

    comp6 = comp5.clone()
    comp6.gpu = "Intel Xe Graphics"
    computer_store.add_computer(comp6)

    comp7 = comp6.clone()
    comp7.cpu = "Intel Core i7"
    computer_store.add_computer(comp7)

    comp8 = comp7.clone()
    comp8.cpu = "AMD Ryzen 9"
    computer_store.add_computer(comp8)

    comp9 = comp8.clone()
    comp9.memory = "64GB RAM"
    computer_store.add_computer(comp9)

    comp10 = comp9.clone()
    comp10.cpu = "Apple M1"
    computer_store.add_computer(comp10)

    computer_store.display_computers()
