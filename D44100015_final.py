#Pascal's triangle
from functools import reduce#import recrucion function
def generate_pascals_triangle(height):#function for generating triangle
    triangle = []
    for i in range(height):
        row = [1] * (i + 1)  # Initialize each row with 1s
        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
	for row in triangle:
		print(' '.join(str(num) for num in row))
height=False
while height==False:
	h=int(input("height of pascal's triangle"))
	if h <1:
		print("invalid input, please enter a integer greater than or equal to 1")
		continue
	else:
		break
d=input('derction of the triangle("normal" "reversed" "left" or "right")')
if d=='normal':	
    pascal_triangle = generate_pascals_triangle(h)
    # Find the maximum length of a row
    max_length = len(' '.join(str(num) for num in pascal_triangle[-1]))
    
    # Print Pascal's triangle with center-aligned rows
    for row in pascal_triangle:
        row_str = ' '.join(str(num) for num in row)
        num_spaces = (max_length - len(row_str)) // 2
        print(' ' * num_spaces + row_str)

elif d=="reversed":
	
    pascal_triangle = generate_pascals_triangle(h)
    pascal_triangle.reverse()  # Reverse the order of rows

    # Find the maximum length of a row
    max_length = len(' '.join(str(num) for num in pascal_triangle[0]))

    # Print Pascal's triangle with center-aligned rows in reversed direction
    for row in pascal_triangle:
        row_str = ' '.join(str(num) for num in row)
        num_spaces = (max_length - len(row_str)) // 2
        print(' ' * num_spaces + row_str)


elif d=="left":	
    pascal_triangle = generate_pascals_triangle(h)
    
    # Find the maximum length of a row
    max_length = len(' '.join(str(num) for num in pascal_triangle[-1]))
    
    # Print Pascal's triangle with right-centered rows
    for row in pascal_triangle:
        row_str = ' '.join(str(num) for num in row)
        num_spaces = max_length - len(row_str)
        print(' ' * num_spaces + row_str)


	
elif d=="right":
	pascal_triangle = generate_pascals_triangle(h)
	
	# Print Pascal's triangle
	print_pascals_triangle(pascal_triangle)