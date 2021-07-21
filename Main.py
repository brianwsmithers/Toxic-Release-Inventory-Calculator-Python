# prompt
print("Toxic Release Inventory Calculator\n")

# block of code for specific gravity
# any floating point number
print("Enter chemicals specific gravity: ")
specificGravity = float(input())

# block of code for concentration
# any floating point number between 0 and 1
print("Enter chemicals concentration: (0.0 - 1.0)")
concentration = float(input())

# block of code for pounds/gal calculation
poundsPerGallon = float(specificGravity) * 8.34

# block of code for threshold
# 10,000 lbs or 25,000 lbs
print("Enter threshold:\n1- 10,000 lbs\n2- 25,000 lbs")

thresholdInt = int(input())
if thresholdInt == 1:
    threshold = 10000
elif thresholdInt == 2:
    threshold = 25000
else:
    threshold = 10000

# block of code to calculate units
# calculation example for 12 fluid ounce aerosol can (Pounds -> Aerosol Can)
# 10,000 lbs * (1 fl. oz. / 8.34 lbs) * 128 fl. oz. ( 1 aerosol can / 12 fl. oz. )

unitsTenOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 10.0)
unitsTwelveOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 12.0)
unitsFifteenOz = threshold * (1.0 / poundsPerGallon) * 128 * (1.0 / 15.0)
unitsGallons = threshold * poundsPerGallon
print("\n\n\nSummary")
print("\nSpecific Gravity -", specificGravity)
print("Concentration -", concentration)
print("Pounds/Gal -", poundsPerGallon)
print("Threshold - " + str(threshold) + " lbs")
print("\nUnits 10 fl. oz. -", round(unitsTenOz))
print("Units 12 fl. oz. -", round(unitsTwelveOz))
print("Units 15 fl. oz. -", round(unitsFifteenOz))
print("Units U.S. Gallons -", round(unitsGallons))
