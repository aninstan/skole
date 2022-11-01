import math as m

class Planet:
    """
    Class for planet objects.

    Parameters: 
        name (str): Name of the planet
        radius (float): Radius of the planet in km
        sun_distance (float): Distance from the sun in million km
        rings = 0 (int): Number of rings the planet has, only specify if more than 0
    """

    def __init__(self, name, radius, sun_distance, rings = 0):

        """ constructor """

        self.name = name
        self.radius = radius
        self.sun_distance = sun_distance
        self.rings = rings
    
    def surface(self):
        surface = 4 * m.pi * self.radius ** 2
        return surface / 1000000 # million km^2

    def volume(self):
        volume = 4 / 3 * m.pi * self.radius ** 3
        return volume / 10000000000 # 10 billion km^3

    def light_to_planet(self):
        speed_of_light = 0.3 # million km per second
        speed = self.sun_distance / speed_of_light
        return speed / 60 # returns minutes



mercury = Planet("Mercury", 2439.7, 58)
venus = Planet("Venus", 6051.8, 108)
earth = Planet("Earth", 6371, 150)

#print(mercury.name, venus.radius, earth.sun_distance)

print(mercury.surface())
print(venus.volume())
print(earth.light_to_planet())