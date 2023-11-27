class Auto:
    def __init__(self, max_speed, weight):
        self.max_speed = max_speed
        self.weight = weight

class Sahkoauto(Auto):
    def __init__(self, max_speed, weight, battery):
        super().__init__(max_speed, weight)
        self.battery = battery


# Test cases for Auto
auto1 = Auto(150, 1000)
assert auto1.max_speed == 150, "Max speed should be 150"
assert auto1.weight == 1000, "Weight should be 1000"

# Test cases for Sahkoauto
sahkoauto1 = Sahkoauto(180, 1200, 500)
assert sahkoauto1.max_speed == 180, "Max speed should be 180"
assert sahkoauto1.weight == 1200, "Weight should be 1200"
assert sahkoauto1.battery == 500, "Battery capacity should be 500"

print("All tests passed!")
