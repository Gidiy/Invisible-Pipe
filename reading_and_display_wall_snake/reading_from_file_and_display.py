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
distance = 5



def vector(x_angle, y_angle, z_angle, length):

    x = length * math.cos(x_angle) * math.cos(y_angle) #yaw =x_angle, pitch = y_angle
    y = length * math.sin(x_angle) * math.cos(y_angle)
    z = length * math.sin(y_angle)
    print(f"in radian x : {x}, y:{y}, z:{z}")
    return [x, y, z]


def degrees_to_radians(degrees):
    return degrees * math.pi / 180

def plot_vector(vec, color):
    global location_x
    global location_y
    global location_z
    print (f"{vec[0],vec[1],vec[2]}")
    text = f"{round(location_x,2)},{round(location_y,2)} , {round(location_z,2)}"
    ax.text(location_x,location_y,location_z,text, color= 'red')
    ax.quiver(location_x, location_y, location_z, vec[0], vec[1], vec[2], color=color)
    location_x += vec[0]
    location_y += vec[1]
    location_z += vec[2]

def clear_plot():
    ax.cla()  # Clear the current axes

def animate(frame):
    global time_elapsed
    global location_x
    global distance
    arduino_data_file = "D:/snake_wall/reading_and_display_wall_snake/txt.txt"  # file_data_location_contain_only_angels

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
                    status, pitch, roll, yaw = map(int, values) #Read line from a text File with data of angle's axis
                    print(f"pitch angle: {pitch}, roll angle:{roll}, yaw angle: {yaw}")
                    plot_vector(vector(degrees_to_radians(-yaw), degrees_to_radians(pitch), degrees_to_radians(roll), distance),color='y')

                    #data of angle's axis -> convert degrees to radians->take 3 angles in radians(Spherical coordinate system)  and length
                    # and return cartesian vector from previous point to the next point then drew it in the 3D graph and update the last point
                except ValueError as e:
                    print(f"Error converting values to integers: {e}")

        ax.quiver(0, 0, 0, 5, 0, 0, color="r")  # x
        ax.quiver(0, 0, 0, 0, 5, 0, color="b")  # y
        ax.quiver(0, 0, 0, 0, 0, 5, color="g")  # z
        ax.autoscale()
        ax.set_title('SneakIn')

ani = animation.FuncAnimation(fig, animate, interval=0.01, frames=10)

plt.show()








