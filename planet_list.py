planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

del planet_list[-1]

rocky_planets = planet_list[0:3]

print("rocky_planets", rocky_planets)

print("planet list", planet_list)

spacecraft = [
    ("Cassini", "Saturn")
    ("Viking", "Mars")
    ("Ulysses", "Jupiter")
    ("Dragonfly", "Titan")
]