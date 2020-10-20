class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()

    def add_all(self, list_of_passengers):
        # first test -adding people to a list from a list
        for person in list_of_passengers:
            self.queue.append(person)
