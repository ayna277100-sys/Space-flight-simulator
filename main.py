#spaceflight simulator
#Version 0.1 just basic gravity (page 1 of coding journal)
G = 6.67430e-11
earth_mass = 5.972e24
earth_radius = 6.371e6
#defining the basic quyanities for the equations 
altitude_km = float(input("enter spacecraft alittude in km please: "))
altitude = altitude_km * 1000
#converted to SI base units
distance_from_earth_centre = earth_radius + altitude
gravity_acceleration = G*earth_mass/distance_from_earth_centre**2
print(gravity_acceleration)

#ability to calculate the spoacecrafts gravitational accelaration at curent altitude
