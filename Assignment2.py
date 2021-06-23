class Example:
    def area(r,pi=3.14):
        return pi*r*r
radius=int(input("Enter the radius: "))
circle_area=Example.area(radius)
print("The area of circle is ",circle_area)