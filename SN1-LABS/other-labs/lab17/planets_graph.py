import matplotlib.pyplot as plt
#data about the planets in our Solar system with units
# "radius": km ,"distance_sun": km  and "orbit_period":days 
planets = {
    "mercury":{"radius": 2439.7,"distance_sun": 5.800e7,"moons": 0,"gas_planet": False, "orbit_period":88.0},
    "venus":{"radius": 6051.8,"distance_sun": 1.082e8,"moons": 0,"gas_planet": False,"orbit_period":224.7},
    "earth":{"radius": 6371,"distance_sun": 1.496e8,"moons": 1,"gas_planet": False,"orbit_period":365.2},
    "mars":{"radius": 3389.5,"distance_sun": 2.279e8,"moons": 2,"gas_planet": False,"orbit_period":687.0},
    "jupiter":{"radius": 69911,"distance_sun": 7.785e8,"moons": 79,"gas_planet": True, "orbit_period":4331},
    "saturn":{"radius": 58232,"distance_sun": 1.433e9,"moons": 83,"gas_planet": True,"orbit_period":10747},
    "uranus":{"radius": 25362,"distance_sun": 2.871e9,"moons": 27,"gas_planet": True,"orbit_period":30589},
    "neptune":{"radius": 24622,"distance_sun": 4.495e9,"moons": 14,"atmosphere": True,"gas_planet": True,"orbit_period":59800}
}
data = [[], [], [], []]
for planet, attr in planets.items():
    x = [attr["distance_sun"] / planets["earth"]["distance_sun"], attr["orbit_period"] / planets["earth"]["orbit_period"]]
    data[0].append(x[0])
    data[1].append(x[1])
    data[2].append(x[0] ** 3)
    data[3].append(x[1] ** 2)
plt.subplot(1, 2, 1)
plt.plot(data[0], data[1], marker="^", color="green", linestyle="dotted")
plt.xlabel("orbital distance in AU")
plt.ylabel("orbital period in years")
plt.subplot(1, 2, 2)
plt.plot(data[2], data[3], marker="v", color="red", linestyle="dotted")
plt.xlabel("orbital distance$\mathregular{^{2}}$ in AU$\mathregular{^{2}}$")
plt.ylabel("orbital period$\mathregular{^{3}}$ in years$\mathregular{^{3}}$")
plt.tight_layout()
plt.show()

