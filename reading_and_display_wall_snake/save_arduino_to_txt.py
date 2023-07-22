import serial
import time
import sys

file_name = sys.argv[1]  # new date for a new txt file
x = 0
points = 10  # points to check


def saving():  # saving function open new file and takes 500 lines of data and saved them. Moreover, if the botton is
    # pushed the system wait until it unpushed.
    file = open(file_name, "w", encoding="utf-8")
    Y = 0
    flag = 0  # flag is have not released yet
    while Y < points:  # SAVE 4 POINTS
        try:  # If the button pressed write to file and wait to the next press
            data = arduino.readline().decode('latin1', errors='ignore').rstrip()
            values = data.split(',')
            status, pitch, roll, yaw = map(int, values)
            print(f"status={status} pitch={pitch} roll={roll} yaw={yaw}")
            while status == 0:
                if status == 0 and flag == 0:
                    file.write(data + "\n")
                    Y += 1
                    print(f"waiting to release botton + {Y}")
                    flag = 1
                data = arduino.readline().decode('latin1', errors='ignore').rstrip()
                values = data.split(',')
                status, pitch, roll, yaw = map(int, values)
                print(f"status={status} pitch={pitch} roll={roll} yaw={yaw}")  # y x z

            flag = 0
        except Exception as e:
            print("An error occurred:", str(e))
    file.close()
    print("File closed")


arduino = serial.Serial('COM7', 9600)

saving()
