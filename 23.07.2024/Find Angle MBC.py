#  https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math
a=int(input().strip())
b=int(input().strip())
angle_radians=math.atan2(a,b)
angle_degrees=math.degrees(angle_radians)
angle_rounded=round(angle_degrees)
print(f"{angle_rounded}\u00B0")
