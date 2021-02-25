import math

g = 9.806
R = 0.0799
s = 0.865
a = -0.00757
m = [0.01, 0.015, 0.02, 0.025, 0.03]
T = [2.011, 1.644, 1.4175, 1.2555, 1.1725]
medel = 0;


for t1 in T:
    m1 = m[T.index(t1)]
    medel += (R * m1 * (g * s * t1**2 - R**2 * math.pi**2 * 2)) / (2 * math.pi**2 * R - a * s * t1**2)
    print "I" + str(T.index(t1) + 1) + ": " + str((R * m1 * (g * s * t1**2 - R**2 * math.pi**2 * 2)) / (2 * math.pi**2 * R - a * s * t1**2))

print "Medel: " + str(medel / len(T))
