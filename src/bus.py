class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        # takes away the need to remove one at a time, 'clear' empties a list
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.passengers.append(passenger)

    def drop_off_at_stop(self, person, bus_stop):
        # Loop through passengers (the list in the init at the top) on the bus
        for passenger in self.passengers:
            # if at their destination (look in the passenger list) = bus stop.name (from bus stop init)
            if passenger.destination == bus_stop.name:
                # remove from the bus (this is passengers.remove(person) from the drop off method)
                self.drop_off(person)
                # add to the bus stop(this is in the bus_stop file add_to_queue method)
                bus_stop.add_to_queue(person)
