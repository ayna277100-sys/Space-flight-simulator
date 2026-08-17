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
#version 0.2 -  adding simple motion
#allow the user to choose the starting speed of their spacecraft 
speed = float(input("enter a starting speed in m/s please: "))
#next give the spacecraft its 2D starting position 
# earth is (0,0) and we use that spacecraft starts at the psotiive x -axis 
x = distance_from_earth_centre
y = 0
#give spacecraft initional velocity 
vx = 0
vy = speed
# now calculkate the spacecraft distance from center of the earth 
distance = (x ** 2 + y**2)**(1/2)
print(distance)
#we have magnitucde of gravitational acceleration we now need to code the direction that the gravity is actring in 
ax = -gravity_acceleration * (x/distance)
ay = -gravity_acceleration * (y/distance)
print("x acceleration", ax)
print("y acceleration", ay)

#day2 V0.2 continued
#so when the rocket is travelling, how much time passes in every simulated loop we use 1 second

time_step = 1
vx = vx+ax*time_step
vy = vy+ay*time_step
print("new vx:", vx)
print("new vy:", vy)
x = x+vx*time_step
y = y+vy*time_step
print("new x:", x)
print("new y:", y)

