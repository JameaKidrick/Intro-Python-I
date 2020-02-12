# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

testEx1 = LatLon(37.2551, -119.61752)

print(f'Latitude is {testEx1.lat:.1f} and Longitude is {testEx1.lon:.1f}')

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

testEx2 = Waypoint('California', 37.2551, -119.61752)

print(f'Latitude is {testEx2.lat:.1f}, Longitude is {testEx2.lon:.1f}, and Name is {testEx2.name}')

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

testEx3 = Geocache('California', 'Level', 'Huge', 37.2551, -119.61752)

print(f'Latitude is {testEx3.lat:.1f}, Longitude is {testEx3.lon:.1f}, Name is {testEx3.name}, its difficulty is {testEx3.difficulty}, and it is {testEx3.size}')

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

newWaypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(f'{newWaypoint.name}, {newWaypoint.lat}, {newWaypoint.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
