#  https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath
z=complex(input().strip())
modulus=abs(z)
phase_angle=cmath.phase(z)
print(modulus)
print(phase_angle)
