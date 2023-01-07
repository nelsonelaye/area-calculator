# This a calculator program for calculating the areas of shape. The shape we're going to be calculating are circle and triangle 

print ("Welcome to my Area Calculator ")

print("What shape do you want to see it area?")
option = input("Enter C for Circle or T for Triangle: ")

if option.lower() == 'c':
    radius = float(input("Enter the radius for shape: "))
    pi = 3.14159
    area = pi * (radius ** 2)
    print ("Area for the circle shape is %s") % (area)

elif option.lower() == 't':
   base = float(input("Enter the base for triangle shape: "))
   height = float(input("Enter the height for the triangle shape: "))
   area = 0.5 * (base * height)
   print ("Area for the triangle shape is %s") % (area)

else:
    print("Invalid input. Enter c or t ")

print("Great job. Goodbye for now")
  
  