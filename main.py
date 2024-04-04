import math

# Annetut arvot
V = 350  # jännite voltteina
e = 1.6e-19  # elektronin varaus coulombeina
m = 9.11e-31  # elektronin massa kilogrammoina
r = 75.2e-3  # säde metreinä (muutettu millimetreistä metreiksi)

# Laske elektronin nopeus potentiaalierosta
E = e * V  # elektronin energia jouleina
v = math.sqrt(2 * E / m)  # elektronin nopeus m/s

# Lorentzin voima on sama kuin keskipakoisvoima magneettikentässä ympyräradalla
# F = mv^2/r on keskipakoisvoima
# F = qvB on Lorentzin voima
# Keskipakoisvoiman ja Lorentzin voiman on oltava yhtä suuret ympyräliikkeessä

# Ratkaistaan B
B = (m * v**2) / (r * e)

print(f"Elektronin nopeus on: {v} m/s")
print(f"Magneettivuon tiheys B on: {B} T")
