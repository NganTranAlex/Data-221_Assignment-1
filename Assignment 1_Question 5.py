# Circle Area Comparison with Validation
import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # check of both radii are positive integers
    if radiusOfCircle1 <= 0 and radiusOfCircle2 <= 0:
        return "Both radii must be positive integers. Please try again."

    #calculate the area of both circles
    areaOfCircle1 = radiusOfCircle1 * radiusOfCircle1 * math.pi # math.pi is the whole pi number instead of only 3.14
    areaOfCircle2 = radiusOfCircle2 * radiusOfCircle2 * math.pi

    if areaOfCircle1 > areaOfCircle2:
        smaller_circle = areaOfCircle2
        larger_circle = areaOfCircle1
    else:
        smaller_circle = areaOfCircle1
        larger_circle = areaOfCircle2

    return ((smaller_circle / larger_circle) * 100)

# print(circleAreaCoverage(4, 5)) # example
print(f"The percentage of the larger circle's area that can be covered by the smaller circle is: {circleAreaCoverage(5,8)}%")



