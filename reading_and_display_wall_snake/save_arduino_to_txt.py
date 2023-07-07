import datetime
import serial
import time

current_datetime = datetime.datetime.now()
datetime_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
#file_name = f"data_from_arduino/{datetime_str}.txt"
file_name = f"txt.txt"
x = 0


def saving():
    file = open(file_name, "w", encoding="utf-8")
    for x in range(500):
        try:
            data = arduino.readline().decode('latin1', errors='ignore').rstrip()
            print(data)
            file.write(data + "\n")
            x += 1

        except Exception as e:
            print("An error occurred:", str(e))
    file.close()
    print("File closed")

arduino = serial.Serial('COM7', 9600)


saving()

