"""
Robert Hamby
December 4, 2019
Day 3 Part 1
https://adventofcode.com/2019/day/3

Wowee, this takes awhile to compute. I know there has to be an
easier and more efficient way to find an intersection, but I 
just can't think of it. My skills are still too limited. One day
I'm going to come back to this and figure it out. Until then, 
run the program and then make some tea, eat something, run a
marathon, or get married. Once you've done that, it'll finally
tell you the answer.
"""

# Opens document, splits at newlines, and returns list
def read_txt(filename):
	info = []

	with open(filename) as text:
		info = text.read().splitlines()

	return info

# Takes split document breaks each element in the list down
# into tuples containing a direction and a length
def parse_instructions(wire_list):
	parsed = []

	for inst in wire_list:
		direction = inst[0]
		length = int(inst[1:])

		parsed.append((direction, length))

	return parsed

# Takes curr_pnt and increases or decreases x or y depending on
# instruction argument and returns an updated point
def update_movements(instruction, curr_pnt):
	direction = instruction[0].upper()
	curr_x = curr_pnt[0]
	curr_y = curr_pnt[1]

	if direction == "U":
		curr_y += 1
	elif direction == "D":
		curr_y += -(1)
	elif direction == "L":
		curr_x += -(1)
	else:
		curr_x += 1

	return (curr_x, curr_y)

# Adds every point between a current point and next point
# into a list, until the end of the instruction set
def get_points(instruction_set):
	curr_point = (0,0) # Starting point
	points = [] # Stores all points

	for instr in instruction_set:
		length = instr[1]
		for i in range(0, length):
			movement = update_movements(instr, curr_point)
			points.append(movement)
			curr_point = movement

	return points

# Checks Every. Single. Point. in wire 1 points for a match
# in wire 2 points
def find_intersections(wire_1_points, wire_2_points):
	intersections = []

	for point in wire_1_points:
		if point in wire_2_points:
			intersections.append(point)

	return intersections

# Uses the manhatten distance formula to compare points
# to find which is closest. Returns the coordinate
def find_closest_point(intersections):
	closest = 9999999999999 #Filler number for comparison
	point = None

	for inter in intersections:
		value = abs(inter[0]) + abs(inter[1])
		if value < closest:
			closest = value
			point = inter

	return (point)


# Write document to list
wires = read_txt("input.txt")

# Break up instructions by comma and parse
wire_1 = parse_instructions(wires[0].split(','))
wire_2 = parse_instructions(wires[1].split(','))

# All points
wire_1_points = get_points(wire_1)
wire_2_points = get_points(wire_2)

# Get intersections
intersections = find_intersections(wire_1_points, wire_2_points)

# After a hundred years, find the closest
closest = find_closest_point(intersections)

print("Closest: {}".format(closest[0]))
