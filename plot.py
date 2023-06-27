import matplotlib.pyplot as plt

# Function to get input points from the user
def get_points():
    points = []
    for i in range(4):
        x = float(input("Enter x-coordinate for point {}: ".format(i+1)))
        y = float(input("Enter y-coordinate for point {}: ".format(i+1)))
        points.append((x, y))
    return points

# Get three points from the user
points = get_points()

# Extract x and y coordinates from the points
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Create a plot and connect the points
plt.plot(x_coords, y_coords, marker='o')

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph Connecting Three Points')

# Show the plot
plt.show()
