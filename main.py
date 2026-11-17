#spaceflight simulator
#Version 0.1 just basic gravity (page 1 of coding journal)
G = 6.67430e-11
earth_mass = 5.972e24
earth_radius = 6.371e6
#defining the basic quyanities for the equations 
altitude_km = float(input("enter starting spacecraft alittude in km: "))
altitude = altitude_km * 1000
#converted to SI base units
distance_from_earth_centre = earth_radius + altitude
gravity_acceleration = G*earth_mass/distance_from_earth_centre**2


#ability to calculate the spoacecrafts gravitational accelaration at curent altitude
#version 0.2 -  adding simple motion
#allow the user to choose the starting speed of their spacecraft 
speed = float(input("enter the spacecraft starting speed in m/s: "))
#next give the spacecraft its 2D starting position 
# earth is (0,0) and we use that spacecraft starts at the psotiive x -axis 
x = distance_from_earth_centre
y = 0
#give spacecraft its initial velocity 
vx = 0
vy = speed
# now calculkate the spacecraft distance from center of the earth (deleted once loop runs its calculated anyways) 


time_step = float(input("enter simulation timne step in seconds: ")) 

# Ask user how long the simulation should run
simulation_time = float(input("Enter total simulation  time in seconds: "))

# Start simulation time at zero
time = 0
#store the simulation history for each time step
x_positions = [x]
y_positions = [y]
vx_values = [vx]
vy_values = [vy]
time_values = [time]

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
    #store the spacecrafts updated state for this time step  
    time = time + time_step
    time_values.append(time)
    x_positions.append(x)
    y_positions.append(y)
    vx_values.append(vx)
    vy_values.append(vy)
   
    
    #asking user how these simulation results should be displayed
exact_values = input("Would you like to see exact values? yes/no: ")

print("\nsimulation results")
print("-"*85)
print( 
    f"{'time (s)': <12}"
     f"{'X Position (m)': <18}"
     f"{'Y Position  (m)': <18}"
     f"{'X Velocity (m/s)': <19}"
     f"{'Y Velocity (m/s)': <19}"
    )
for i in range (len(time_values)):
  
  if exact_values == "yes":
    time_display = time_values[i]
    x_display = x_positions[i]
    y_display = y_positions[i]
    vx_display = vx_values[i]
    vy_display = vy_values[i]
  else:
    
    time_display = round(time_values[i], 2)
    x_display = round(x_positions[i], 2)
    y_display = round(y_positions[i],2)
    vx_display = round(vx_values[i], 2)
    vy_display = round(vy_values[i], 2)
  print(
        f"{time_display:<12}"
        f"{x_display:<18}"
        f"{y_display:<18}"
        f"{vx_display:<19}"
        f"{vy_display:<19}"
    )
    
print("-" * 85)
    