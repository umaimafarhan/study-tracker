# Unit Converter Project
# Converts between meters, kilometers, and centimeters

def convert_length(value, from_unit, to_unit):
    units = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    # Convert to meters first
    value_in_meters = value * units[from_unit]

    # Convert meters to target
    return value_in_meters / units[to_unit]


print("Unit Converter")
value = float(input("Enter value: "))
from_unit = input("Convert from (cm/m/km): ").lower()
to_unit = input("Convert to (cm/m/km): ").lower()

result = convert_length(value, from_unit, to_unit)
print(f"{value} {from_unit} = {result} {to_unit}")
