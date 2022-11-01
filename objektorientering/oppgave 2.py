class Planet:
    def __init__(self, name, radius, sun_distance, rings = 0):
        self.name = name
        self.sun_distance = sun_distance
        self.radius = radius
        self.rings = rings

mercury = Planet("Mercury", 58, 2439.7)
venus = Planet("Venus", 108, 6051.8)
earth = Planet("Earth", 150, 6371)

print(mercury.name, venus.radius, earth.sun_distance)