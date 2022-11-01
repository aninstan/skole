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

        """ konstructor """

        self.name = name
        self.sun_distance = sun_distance
        self.radius = radius
        self.rings = rings
    
    def surface(self):
        return 4 * m.pi * self.radius ** 3



mercury = Planet("Mercury", 58, 2439.7)
venus = Planet("Venus", 108, 6051.8)
earth = Planet("Earth", 150, 6371)

print(mercury.name, venus.radius, earth.sun_distance)
