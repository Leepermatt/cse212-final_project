class TrainCar:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

class Train:
    def __init__(self):
        self.head = None

    def add_car(self, cargo):
        new_car = TrainCar(cargo)
        if self.head is None:
            self.head = new_car
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_car

    def remove_car(self):
        if self.head is None:
            print("Train is already empty")
        else:
            removed_car = self.head
            self.head = self.head.next
            return removed_car.cargo

    def display_train(self):
        current = self.head
        print("Train cars:")
        while current:
            print(current.cargo, end=" -> ")
            current = current.next
        print("None")

# Example usage:
train = Train()

# Adding train cars
train.add_car("Passenger")
train.add_car("Cargo")
train.add_car("Oil Tanker")
train.add_car("Boxcar")

# Displaying train cars
train.display_train()

# Removing a train car
removed_car = train.remove_car()
print(f"Removed train car: {removed_car}")

# Displaying train cars after removal
train.display_train()