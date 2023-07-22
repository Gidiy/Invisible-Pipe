import subprocess
import sys #for system exit

 #This code run 2 scripts of python. The first update a 3D graph from  a text file withe the data from arduino,
 #The second file save the arduino data of diractions in 3 Axis into a text file.

# Define the paths proto the Python scripts
script1_path = 'reading_from_file_and_display.py'
script2_path = 'save_arduino_to_txt.py'
x = 0

# Run script1.py in a separate process
process1 = subprocess.Popen(['python', script1_path])

# Run script2.py in a separate process
process2 = subprocess.Popen(['python', script2_path])


# Wait for both processes to complete
process1.wait()
process2.wait()

print("Great Job")


sys.exit()
