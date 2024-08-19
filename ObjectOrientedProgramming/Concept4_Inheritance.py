class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} (<{self.connected_by}>) and {self.connected} got created successfully"

    def disconnect(self):
        self.connected = False
        print("Disconnected successfully")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity


printer = Device("Printer", "USB")
print(printer)
printer.disconnect()
