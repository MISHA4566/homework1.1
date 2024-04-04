class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed


v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)


result = v1 > v2
print(result)


vehicles = [v1, v2]

sorted_vehicles = sorted(vehicles, key=lambda x: x.speed)
print(sorted_vehicles)
