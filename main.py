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

time_step = float(input("enter your time step pleaseee: ")) 

# Ask user how long the simulation should run
simulation_time = float(input("Enter total simulation time in seconds: "))

# Start simulation time at zero
time = 0

# Repeat the physics calculations until simulation time is reached
while time < simulation_time:
    # Calculate current distance from Earth's centre
    distance = (x**2 + y**2) ** (1/2)
    # Recalculate gravitational acceleration at the new distance
    gravity_acceleration = G * earth_mass / distance**2
    # Calculate direction of gravitational acceleration
    ax = -gravity_acceleration * (x / distance)
    ay = -gravity_acceleration * (y / distance)
    # Acceleration changes velocity
    vx = vx + ax * time_step
    vy = vy + ay * time_step
    x = x + vx * time_step
    y = y + vy * time_step
    time = time + time_step


print("Final x:", x)
print("Final y:", y)
print("Final vx:", vx)
print("Final vy:", vy)


