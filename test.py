import matplotlib.pyplot as plt


# Data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 5, 3, 7, 6]

# Create a line plot with markers
plt.plot(x_values, y_values, marker='o', linestyle='--', color='blue')

# Add title and labels
plt.title("Sample Data Visualization")
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")

# Add a grid for better readability
plt.grid(True)

# Display the plot
plt.show()