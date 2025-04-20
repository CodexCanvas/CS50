""" prompt the user for a an amount of mass in Kg
 and give them the equivalent in energy in Joules"""

print("E = mc^2")

mass = input("Enter mass in Kg: ")
try:
    mass = float(mass)
except ValueError:  
    print("Invalid input. Please enter a number.")
    exit(1)
if mass < 0:
    print("Mass cannot be negative.")
    exit(1)

energy = mass * 300000000**2  # E = mc^2
print(f"The energy equivalent of {mass} Kg is {int(energy):,} Joules")
