# SUVAT Equation Calculator for Physics Mechanics

def calculate_missing(u=None, v=None, a=None, t=None, s=None):
    # Example: If you give u, a, and t → returns v
    if u is not None and a is not None and t is not None:
        return u + a * t
    if v is not None and a is not None and t is not None:
        return v - a * t
    if u is not None and v is not None and t is not None:
        return (u + v) / 2 * t
    return None

print("SUVAT Calculator")
print("Provide known values (leave unknowns blank)")

def get_val(label):
    x = input(f"{label}: ")
    return float(x) if x else None

u = get_val("Initial velocity (u)")
v = get_val("Final velocity (v)")
a = get_val("Acceleration (a)")
t = get_val("Time (t)")
s = get_val("Displacement (s)")

result = calculate_missing(u, v, a, t, s)
print("\nCalculated value:", result)
