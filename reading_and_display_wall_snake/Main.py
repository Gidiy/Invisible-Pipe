import subprocess
import sys  # for system exit
import datetime

# This code run 2 scripts of python. The first update a 3D graph from  a text file withe the data from arduino,
# The second file save the arduino data of diractions in 3 Axis into a text file.
# The two scripts get a date for a creation of a new txt file
current_datetime = datetime.datetime.now()
datetime_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"data_from_arduino/{datetime_str}.txt"

script1_path = 'reading_from_file_and_display.py'
script2_path = 'save_arduino_to_txt.py'

process1 = subprocess.Popen(['python', script1_path, str(file_name)])

process2 = subprocess.Popen(['python', script2_path, str(file_name)])

process1.wait()
process2.wait()

print("Great Job")

sys.exit()
