import threading
import time
import serial
from redbox import detect_redbox  # Import your red box detection function

# Replace with your DonkeyCar controller or custom path logic
from donkeycar.parts.controller import LocalWebController

# Serial communication with Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Update this port as needed
time.sleep(2)  # Allow time for Arduino to initialize


detected = False
at_home = False

def donkeycar_path_control():
    global detected
    controller = LocalWebController()

    current_path = "follow_path"
    controller.run_threaded(mode=current_path)

    while True:
        if detected:
            current_path = "return_home"
        else:
            current_path = "follow_path"

        controller.run_threaded(mode=current_path)
        time.sleep(0.1)

def control_electromagnet():
    global detected, at_home
#this happens over arduino cli
    while True:
        if detected:
            arduino.write(b'ON\n')  
        elif at_home:
            arduino.write(b'OFF\n')  
        time.sleep(0.1)

def detect_object():
    global detected
    while True:
        detected = detect_redbox()  # True if red box is detected
        time.sleep(0.1)

def check_home_reached():
    global at_home
    while True:
        # Replace this with your actual method to detect home arrival
        at_home = False  # Set to True when DonkeyCar reaches home
        time.sleep(0.1)

# Start all threads
threads = [
    threading.Thread(target=donkeycar_path_control),
    threading.Thread(target=control_electromagnet),
    threading.Thread(target=detect_object),
    threading.Thread(target=check_home_reached)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
