import math 

def circle_stats(r):
    area =  math.pi * r**2
    circumference = 2*math.pi *r
    return area, circumference

a, c = circle_stats(5)
print("area: ", round(a, 2) , "circumference: ", round(c, 2))