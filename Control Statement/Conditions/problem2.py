pie = 3.147
radius = input("Enter radius: ")

#presence of float (.)
if '.' in radius:
    radius = float(radius)
    area_of_circle = radius*radius*pie
    print("Area of circle:", area_of_circle)
else:
    print("Input only float values to calculate the radius")
    



