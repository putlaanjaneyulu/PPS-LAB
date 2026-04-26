import math
def orbit_length(r):
    return 2 * math.pi * r
def orbit_velocity(r, T):
    return (2 * math.pi * r) / T
r = float(input("Enter the radius: "))
T = float(input("Enter the Orbital period: "))
circumference = orbit_length(r)
velocity = orbit_velocity(r, T)
print(f"Orbital Circumference: {circumference:.2f} km")
print(f"Orbital Velocity: {velocity:.2f} km/s")
