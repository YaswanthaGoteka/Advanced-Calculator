# import math
#
# shape_list = ['triangle', 'rhombus', 'diamond', 'rectangle', 'square']
# extra_list = ['no diagonal', 'no height','height', 'area', 'hypotenuse', 'base', 'altitude', 'diagonal', 'sides', 'area-and-diagonal', 'height-hypotenuse']
#
# print("These are your options:")
# print(shape_list)
# shape_input = input("What shape do you want to find the info of? ").lower()
#
# if shape_input not in shape_list:
#     print("Your input isn't in the options above")
#     quit()
#
# # --- TRIANGLE ---
# if shape_input == "triangle":
#     triangle_list = ['height', 'area', 'hypotenuse', 'base', 'altitude', 'height-hypotenuse']
#     print("Options:", triangle_list)
#     triangle_find = input("What do you want to find in a triangle? ").lower()
#
#     if triangle_find in triangle_list:
#         if triangle_find == 'area':
#             height = input("Height: ")
#             base = input("Base: ")
#             print("Area:", (float(base) * float(height)) / 2)
#
#         elif triangle_find == 'height-hypotenuse':
#             angle_type = input("Is the angle 'cos' or 'sin' to hypotenuse? ")
#             base = float(input('Base: '))
#             angle = float(input('Angle (degrees): '))
#             angle_rad = math.radians(angle)
#
#             if angle_type == 'cos':
#                 hypotenuse = base / math.cos(angle_rad)
#             elif angle_type == 'sin':
#                 hypotenuse = base / math.sin(angle_rad)
#             else:
#                 print("Invalid angle type.")
#                 quit()
#
#             print('Hypotenuse:', hypotenuse)
#             height = math.sqrt(hypotenuse**2 - base**2)
#             print('Height:', height)
#
#         elif triangle_find == 'hypotenuse':
#             side1 = float(input('Side 1: '))
#             side2 = float(input('Side 2: '))
#             hypotenuse = math.sqrt(side1**2 + side2**2)
#             print('Hypotenuse:', hypotenuse)
#
#         elif triangle_find == 'base':
#             method = input("Find using 'altitude' or 'sides'? ").lower()
#             if method == 'altitude':
#                 area = float(input("Area: "))
#                 height = float(input("Height: "))
#                 base = (2 * area) / height
#                 print("Base:", base)
#             elif method == 'sides':
#                 side1 = float(input("Side 1: "))
#                 side2 = float(input("Side 2: "))
#                 hypotenuse = float(input("Hypotenuse: "))
#                 base = math.sqrt(hypotenuse**2 - side2**2)
#                 print("Base:", base)
#             else:
#                 print("Invalid option for base calculation.")
#     else:
#         print('Error, cannot calculate value.')
#         quit()
#
# # --- RHOMBUS / DIAMOND ---
# elif shape_input == "rhombus" or shape_input == "diamond":
#     rhombus_list = ['diagonal', 'sides', 'area', 'height', 'area-and-diagonal']
#     print("Options:", rhombus_list)
#     rhombus_find = input("What do you want to find in a rhombus? ").lower()
#
#     if rhombus_find == 'area-and-diagonal':
#         print('If you only have one diagonal, input "one diagonal" in Diagonal 1.')
#         diagonal1 = input("Diagonal 1: ")
#         if diagonal1 == "one diagonal":
#             side = float(input("Side: "))
#             diagonal2 = float(input("Diagonal 2: "))
#             diagonal1_val = math.sqrt(4 * side**2 - diagonal2**2)
#             print('Missing Diagonal:', diagonal1_val)
#             print("Area:", (diagonal1_val * diagonal2) / 2)
#         else:
#             diagonal1 = float(diagonal1)
#             diagonal2 = float(input("Diagonal 2: "))
#             print("Area:", (diagonal1 * diagonal2) / 2)
#
#     elif rhombus_find == 'area':
#         d1 = float(input("Diagonal 1: "))
#         d2 = float(input("Diagonal 2: "))
#         print("Area:", (d1 * d2) / 2)
#
#     elif rhombus_find == 'sides':
#         d1 = float(input("Diagonal 1: "))
#         d2 = float(input("Diagonal 2: "))
#         side = math.sqrt((d1/2)**2 + (d2/2)**2)
#         print("Side Length:", side)
#
#     elif rhombus_find == 'height':
#         side = float(input("Side: "))
#         angle = float(input("Angle (in degrees): "))
#         height = side * math.sin(math.radians(angle))
#         print("Height:", height)
#
# # --- RECTANGLE / SQUARE ---
# elif shape_input == "rectangle" or shape_input == "square":
#     print("If your", shape_input, "has a diagonal then input 'one diagonal' in Side 1.")
#     print("If your", shape_input, "has two diagonals then input 'two diagonals' in Side 1.")
#     print('*Note: If your diagonal is half-length, double it before input*')
#
#     side1 = input('Side 1: ').lower()
#
#     if side1 == 'one diagonal':
#         diagonal1 = float(input('Diagonal 1: '))
#         side2 = float(input('Side 2: '))
#         missing_side = math.sqrt(diagonal1**2 - side2**2)
#         area = missing_side * side2
#         print('Missing Side:', missing_side)
#         print('Area:', area)
#
#     elif side1 == 'two diagonals':
#         diagonal1 = float(input('Diagonal 1: '))
#         diagonal2 = float(input('Diagonal 2: '))
#         side_a = diagonal1 / math.sqrt(2)
#         side_b = diagonal2 / math.sqrt(2)
#         print('Side A:', side_a)
#         print('Side B:', side_b)
#         print('Area:', side_a * side_b)
#
#     else:
#         try:
#             side1 = float(side1)
#             side2 = float(input('Side 2: '))
#             print("Area:", side1 * side2)
#             diagonal = math.sqrt(side1**2 + side2**2)
#             print("Diagonal:", diagonal)
#         except:
#             print("Invalid input for sides.")
#
# else:
#     print("Shape not recognized.")


# import pandas as pd
# list_value = []
# user_list = []
# while True:
#     user = input("Enter Data Frame Column Title (Or Enter To Exit): ")
#     if user == '':
#         break
#     while True:
#         value = input(f"Enter Value For The Column (Or 'done' To Stop Adding Values): ")
#         if value == 'done':
#             break
#         list_value.append(value)
#
# df = pd.DataFrame({user_list: list_value})
#
# print(df)

