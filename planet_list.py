planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

del planet_list[-1]

rocky_planets = planet_list[0:4]

print("rocky_planets", rocky_planets)

print("planet list", planet_list)

spacecrafts = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars"),
    ("Ulysses", "Jupiter"),
    ("Dragonfly", "Titan")
]


for planet in planet_list:
    print(planet)
    for spacecraft in spacecrafts:
        if planet == spacecraft[1]:
            print("-" + spacecraft[0])
        