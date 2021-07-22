import sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

# Initialize variables
specificGravity = 0
concentration = 0
threshold = 0

# Program greeting
print("Toxic Release Inventory Calculator\n")

print("Enter chemicals specific gravity: ")
i = 0
while i < 3:
    try:
        specificGravity = float(input())
        if specificGravity > 0:
            break
        elif specificGravity == 0:
            print("You must enter a number greater than zero.")
            if i == 2:  # Exit program after 3 attempts
                print("Program exiting due to 3 invalid entries.")
                sys.exit(1)
            else:
                i += 1
    except ValueError:
        print("You did not enter a decimal or integer value.")
        if i == 2:
            print("Program exiting due to 3 invalid entries.")
            sys.exit(1)
        else:
            i += 1

print("Enter chemicals concentration: (0.0 - 1.0)")
i = 0
while i < 3:
    try:
        concentration = float(input())
        if concentration < 0 or concentration <= 1.0:
            break
        elif concentration <= 0 or concentration > 1.0:
            print("Concentration must be greater than 0.0 and less than or equal to 1.0")
            if i == 2:  # Exit program after 3 attempts
                print("Program exiting due to 3 invalid entries.")
                sys.exit(1)
            else:
                i += 1
    except ValueError:
        print("You did not enter a decimal or integer value.")
        if i == 2:
            print("Program exiting due to 3 invalid entries.")
            sys.exit(1)
        else:
            i += 1

poundsPerGallon = (float(specificGravity) * 8.34) * concentration

print("Enter threshold: (1 or 2) \n1- 10,000 lbs\n2- 25,000 lbs")
i = 0
while i < 3:
    try:
        thresholdInt = int(input())
        if thresholdInt == 1:
            threshold = 10000
            break
        elif thresholdInt == 2:
            threshold = 25000
            break
        else:
            print("You did not enter a valid choice.")
            if i == 2:  # Exit program after 3 attempts
                print("Program exiting due to 3 invalid entries.")
                sys.exit(1)
            else:
                i += 1
    except ValueError:
        print("You did not enter a valid choice.")
        if i == 2:
            print("Program exiting due to 3 invalid entries.")
            sys.exit(1)
        else:
            i += 1

# block of code to calculate units
# calculation example for 12 fluid ounce aerosol can (Pounds -> Aerosol Can)
# unitsTwelveOz = 10,000 lbs * (1 fl. oz. / 8.34 lbs) * 128 fl. oz. ( 1 aerosol can / 12 fl. oz. )
if threshold == 10000 or threshold == 25000:
    unitsTenOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 10.0)
    unitsTwelveOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 12.0)
    unitsFifteenOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 15.0)
    unitsGallons = threshold * (1.0 / poundsPerGallon)
else:
    sys.exit(1)

#  Cmd prompt summary
print("\n\nSummary")
print("\nSpecific Gravity -", specificGravity)
print("Concentration -", concentration)
print("Pounds/Gal -", poundsPerGallon)
print("Threshold - " + str(threshold) + " lbs")

print("\n10 fl. oz. Aerosol Cans -", round(unitsTenOz))
print("12 fl. oz. Aerosol Cans -", round(unitsTwelveOz))
print("15 fl. oz. Aerosol Cans -", round(unitsFifteenOz))
print("U.S. Gallons -", round(unitsGallons))

# Code block to create text file
today = date.today()
i = 0  # Name control
a = 0  # Counter control
while a < 99:  # Program will attempt to make up to 99 different files if duplicate is found.
    try:
        if a == 0:
            file = open("TRI Calculation " + str(today) + ".txt", "x")
            file.write("TRI Calculation Summary\n")
            file.write("\nSpecific Gravity - " + str(specificGravity))
            file.write("\nConcentration - " + str(concentration))
            file.write("\nPounds/Gal - " + str(poundsPerGallon))
            file.write("\nThreshold - " + str(threshold) + " lbs")
            file.write("\n\n10 fl. oz. Aerosol Cans - " + str(round(unitsTenOz)))
            file.write("\n12 fl. oz. Aerosol Cans - " + str(round(unitsTwelveOz)))
            file.write("\n15 fl. oz. Aerosol Cans - " + str(round(unitsFifteenOz)))
            file.write("\nU.S. Gallons - " + str(round(unitsGallons)))
            file.close()
            break
        else:
            file = open("TRI Calculation " + str(today) + " (" + str(i) + ")" + ".txt", "x")
            file.write("TRI Calculation Summary\n")
            file.write("\nSpecific Gravity - " + str(specificGravity))
            file.write("\nConcentration - " + str(concentration))
            file.write("\nPounds/Gal - " + str(poundsPerGallon))
            file.write("\nThreshold - " + str(threshold) + " lbs")
            file.write("\n\n10 fl. oz. Aerosol Cans - " + str(round(unitsTenOz)))
            file.write("\n12 fl. oz. Aerosol Cans - " + str(round(unitsTwelveOz)))
            file.write("\n15 fl. oz. Aerosol Cans - " + str(round(unitsFifteenOz)))
            file.write("\nU.S. Gallons - " + str(round(unitsGallons)))
            file.close()
            break
    except FileExistsError:
        i += 1
        a += 1

# Code block for Visual Summary Bar Chart
x = np.array(["10 Fl. Oz.", "12 Fl. Oz", "15 Fl. Oz.", "U.S. Gal"])
y = np.array([round(unitsTenOz), round(unitsTwelveOz), round(unitsFifteenOz), round(unitsGallons)])
plt.bar(x, y)
plt.xlabel("Units of Measurement")
plt.ylabel("Number of Units")

# Save graph image using previous control variables
if a == 0:
    plt.draw()
    plt.savefig("TRI Calculation " + str(today) + ".png", dpi=100)
    plt.show()
else:
    plt.draw()
    plt.savefig("TRI Calculation " + str(today) + " (" + str(i) + ")" + ".png", dpi=100)
    plt.show()
