import math

class Truck:
    def __init__(self, current_location, total_dist, fuel_efficiency, capacity, name):
        self.current_location = current_location
        self.total_dist = total_dist 
        self.fuel_efficiency = fuel_efficiency  
        self.capacity = capacity
        self.name = name  
    def set_truck_location(self, new_location):
        self.current_location = new_location

    def add_mileage(self, additional_miles):
        self.total_dist += additional_miles

    def fuel_consumption(self):
        fuel_used = self.total_dist / self.fuel_efficiency
        return fuel_used

    def check_maintenance(self):
        if self.total_dist > 10000:
            return True
        else:
            return False

def assign_trucks_to_deliveries(deliveries, trucks):
    unassigned_deliveries = deliveries[:]
    assigned_trucks = []

    for delivery in deliveries:
        delivery_size, delivery_destination = delivery
        min_distance = 1000000000
        assigned_truck = None

        for truck in trucks:
            truck_location = truck.current_location
            distance = math.dist(truck_location, delivery_destination)

            if distance < min_distance and truck.capacity >= delivery_size:
                min_distance = distance
                assigned_truck = truck

        if assigned_truck:
            assigned_truck.add_mileage(math.dist(assigned_truck.current_location, delivery_destination))
            assigned_trucks.append((assigned_truck.name, delivery))
            assigned_truck.set_truck_location(delivery_destination)
            unassigned_deliveries.remove(delivery)

    return assigned_trucks

list_of_deliveries = [
    (200, (15, 15)),
    (250, (30, 30)),
    (150, (10, 10)),
    (100, (50, 50)),
    (120, (12, 18))
]

trucks = [
    Truck((20, 20), 0, 10, 200, 'mahindra'),
    Truck((15, 15), 0, 12, 250, 'Tata'),
    Truck((18, 19), 0, 9, 300, 'Ashok Leyland')
]

# Assign trucks to deliveries
assigned_trucks = assign_trucks_to_deliveries(list_of_deliveries, trucks)

for truck, delivery in assigned_trucks:
    print(f"Delivery of size {delivery[0]} to destination {delivery[1]} assigned to truck {truck}.")
