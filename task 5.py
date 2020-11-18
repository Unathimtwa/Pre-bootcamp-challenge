# Calculating area of a triangle is dependent on the base and height in this formula - Area = 1/2.bh
# And so the user will be prompted to enter all three sides of the triangle to determine area.

Triangle_base = input("enter base: ")
Triangle_height = input("enter height: ")
Triangle_other_side = input("Please enter other side: ")
area = 1/2 * int(Triangle_base) * int(Triangle_base)

print(area)
