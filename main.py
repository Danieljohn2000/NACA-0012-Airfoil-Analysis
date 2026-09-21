import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. AIRFOIL SETTINGS
# ============================================================

chord = 1.0

num_points = 200

angle_of_attack = 5.0


# ============================================================
# 2. CREATE NACA 0012 AIRFOIL
# ============================================================

x = np.linspace(0, chord, num_points)

thickness = 0.12


# NACA 4-digit airfoil thickness equation
yt = 5 * thickness * (
    0.2969 * np.sqrt(x)
    - 0.1260 * x
    - 0.3516 * x**2
    + 0.2843 * x**3
    - 0.1015 * x**4
)


# Upper and lower surfaces
x_upper = x
y_upper = yt

x_lower = x
y_lower = -yt


# ============================================================
# 3. CALCULATE LIFT COEFFICIENT
# ============================================================

alpha_rad = np.radians(angle_of_attack)

Cl = 2 * np.pi * alpha_rad


# ============================================================
# 4. CALCULATE PRESSURE COEFFICIENT
# ============================================================

# Simple pressure coefficient model
Cp_upper = 1 - (
    1 + 2 * np.pi * alpha_rad
) ** 2

Cp_lower = 1 - (
    1 - 2 * np.pi * alpha_rad
) ** 2


# ============================================================
# 5. DISPLAY AIRFOIL SHAPE
# ============================================================

plt.figure(figsize=(10, 4))

plt.plot(
    x_upper,
    y_upper,
    label="Upper Surface"
)

plt.plot(
    x_lower,
    y_lower,
    label="Lower Surface"
)

plt.xlabel("x / c")
plt.ylabel("y / c")

plt.title("NACA 0012 Airfoil")

plt.axis("equal")

plt.grid()

plt.legend()

plt.tight_layout()

plt.savefig(
    "naca0012_geometry.png",
    dpi=300
)

plt.show()


# ============================================================
# 6. PLOT PRESSURE COEFFICIENT
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    x,
    Cp_upper,
    label="Upper Surface"
)

plt.plot(
    x,
    Cp_lower,
    label="Lower Surface"
)

plt.xlabel("x / c")
plt.ylabel("Pressure Coefficient (Cp)")

plt.title(
    f"NACA 0012 Pressure Distribution "
    f"at {angle_of_attack}° Angle of Attack"
)

plt.gca().invert_yaxis()

plt.grid()

plt.legend()

plt.tight_layout()

plt.savefig(
    "naca0012_pressure_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# 7. DISPLAY RESULTS
# ============================================================

print("====================================")
print("NACA 0012 AIRFOIL ANALYSIS")
print("====================================")

print(f"Chord length: {chord} m")

print(
    f"Angle of attack: "
    f"{angle_of_attack} degrees"
)

print(
    f"Lift coefficient (Cl): "
    f"{Cl:.4f}"
)

print("====================================")