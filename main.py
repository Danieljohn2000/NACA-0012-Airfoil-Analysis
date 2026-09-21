import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. AIRFOIL SETTINGS
# ============================================================

chord = 1.0
thickness = 0.12

num_points = 200

angle_of_attack = 5.0


# ============================================================
# 2. CREATE NACA 0012 AIRFOIL
# ============================================================

x = np.linspace(0.001, chord, num_points)

# NACA 0012 thickness equation
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
# 3. ANGLE OF ATTACK
# ============================================================

alpha_deg = angle_of_attack
alpha_rad = np.radians(alpha_deg)


# ============================================================
# 4. LIFT COEFFICIENT
# ============================================================

# Thin-airfoil approximation for a symmetric airfoil

Cl = 2 * np.pi * alpha_rad


# ============================================================
# 5. SIMPLE PRESSURE DISTRIBUTION MODEL
# ============================================================

# Avoid division by zero near the leading edge
x_safe = np.maximum(x, 0.001)


# Approximate velocity-change term
velocity_change = (
    2 * alpha_rad
    * np.sqrt((1 - x_safe) / x_safe)
)


# Upper surface
Cp_upper = 1 - (1 + velocity_change) ** 2


# Lower surface
Cp_lower = 1 - (1 - velocity_change) ** 2


# Limit extreme numerical values near the leading edge
Cp_upper = np.clip(Cp_upper, -10, 2)
Cp_lower = np.clip(Cp_lower, -10, 2)


# ============================================================
# 6. PLOT AIRFOIL GEOMETRY
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

plt.title("NACA 0012 Airfoil Geometry")

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
# 7. PLOT PRESSURE DISTRIBUTION
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
plt.ylabel("Pressure Coefficient, Cp")

plt.title(
    f"NACA 0012 Pressure Distribution "
    f"at {angle_of_attack}° Angle of Attack"
)

# Conventional aerodynamic Cp plots
# have negative Cp upward
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
# 8. PRINT RESULTS
# ============================================================

print()
print("========================================")
print("       NACA 0012 AIRFOIL ANALYSIS")
print("========================================")

print(f"Chord length:       {chord:.2f} m")
print(f"Maximum thickness:  {thickness * 100:.1f}%")
print(f"Angle of attack:    {angle_of_attack:.1f} degrees")

print()
print(f"Lift coefficient:    Cl = {Cl:.4f}")

print()
print("Results saved as:")
print("1. naca0012_geometry.png")
print("2. naca0012_pressure_distribution.png")

print("========================================")