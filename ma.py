import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Plotting with the correct argument (marker="o")
plt.plot(x, y, marker="o")

# Customization
plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)

# Display the plot
plt.show()