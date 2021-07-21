import sys

print("Toxic Release Inventory Calculator\n")

print("Enter chemicals specific gravity: ")
try:
    specificGravity = float(input())
    if specificGravity == 0:
        print("You must enter a number greater than zero.")
        sys.exit(1)
except ValueError:
    print("You did not enter a decimal or integer value.")
    sys.exit(1)

print("Enter chemicals concentration: (0.0 - 1.0)")
try:
    concentration = float(input())
    if concentration <= 0 or concentration > 1.0:
        print("Concentration must be greater than 0.0 and less than or equal to 1.0")
        sys.exit(1)
except ValueError:
    print("You did not enter a decimal or integer value.")
    sys.exit(1)

poundsPerGallon = (float(specificGravity) * 8.34) * concentration

print("Enter threshold: (1 or 2) \n1- 10,000 lbs\n2- 25,000 lbs")
try:
    thresholdInt = int(input())
    if thresholdInt == 1:
        threshold = 10000
    elif thresholdInt == 2:
        threshold = 25000
    else:
        print("You did not enter a valid choice.")
        sys.exit(1)
except ValueError:
    print("You did not enter a valid choice.")
    sys.exit(1)

# block of code to calculate units
# calculation example for 12 fluid ounce aerosol can (Pounds -> Aerosol Can)
# unitsTwelveOz = 10,000 lbs * (1 fl. oz. / 8.34 lbs) * 128 fl. oz. ( 1 aerosol can / 12 fl. oz. )
if threshold is not None:
    unitsTenOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 10.0)
    unitsTwelveOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 12.0)
    unitsFifteenOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 15.0)
    unitsGallons = threshold * (1.0 / poundsPerGallon)
else:
    print("Threshold cannot be null")
    sys.exit(1)

print("\n\n\nSummary")
print("\nSpecific Gravity -", specificGravity)
print("Concentration -", concentration)
print("Pounds/Gal -", poundsPerGallon)
print("Threshold - " + str(threshold) + " lbs")

print("\n10 fl. oz. Aerosol Cans -", round(unitsTenOz))
print("12 fl. oz. Aerosol Cans -", round(unitsTwelveOz))
print("15 fl. oz. Aerosol Cans -", round(unitsFifteenOz))
print("U.S. Gallons -", round(unitsGallons))
