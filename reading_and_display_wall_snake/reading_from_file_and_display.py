import math
import random
import serial
import time
import os  # Import the 'os' module for file-related operations
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

location_x = 0
location_y = 0
location_z = 0
time_elapsed = 0

def vector(x_angle, y_angle, z_angle, vector_length):
    x = vector_length * math.sin(x_angle)
    y = vector_length * math.sin(y_angle)
    z = vector_length * math.sin(z_angle)
    return [x, y, z]

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

def plot_vector(vec, color):
    global location_x
    global location_y
    global location_z

    ax.quiver(location_x, location_y, location_z, vec[0], vec[1], vec[2], color=color)
    location_x += vec[0]
    location_y += vec[1]
    location_z += vec[2]

def clear_plot():
    ax.cla()  # Clear the current axes

def animate(frame):
    global time_elapsed
    arduino_data_file = "D:/snake_wall/reading_and_display_wall_snake/txt.txt"  # file_data_location

    # Check if the file has been modified
    modified = os.stat(arduino_data_file).st_mtime

    if modified > time_elapsed:
        time_elapsed = modified  # Update the last modified time
        
        clear_plot()  # Clear the plot

        with open(arduino_data_file, "r") as file:
            lines = file.readlines()

            for line in lines:
                values = line.strip().split(',')

                try:
                    status, pitch, roll, yaw = map(int, values)
                    plot_vector(vector(degrees_to_radians(pitch), degrees_to_radians(roll), degrees_to_radians(yaw), math.sqrt(5)), color='y')

                except ValueError as e:
                    print(f"Error converting values to integers: {e}")

        ax.autoscale()
        ax.set_title('SneakIn')

ani = animation.FuncAnimation(fig, animate, interval=0.01, frames=10)

plt.show()







