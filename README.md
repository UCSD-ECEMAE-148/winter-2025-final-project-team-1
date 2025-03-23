# Autonomous Search and Rescue for Interplanetary Missions
  
![image](https://github.com/UCSD-ECEMAE-148/winter-2025-final-project-team-1/blob/main/images/robot.jpg)

<p align="center">
  ECE-MAE-148 Final Project
  <br> Team 1 (Winter 2025)
  <br> Group Members: Jackson Goenawan (jgoenawan@ucsd.edu), Vaibhav Maloo (vmaloo@ucsd.edu), Giselle Romo (gromo@ucsd.edu), Sabrina Wu (sywu@ucsd.edu)
  </p>

  
<h2>Primary Goal</h2>
Develop an autonomous vehicle capable of simulating a search-and-rescue mission in an interplanetary environment.

Tasks would include:

- **Object Detection & Recognition**
- **Real-Time Mapping and Path Planning with GPS**
- **Object Retrieval**
  - A successful mission where an object is “found and rescued” and an unsuccessful mission where the robot is forced to return to base coordinates

[Final Presentation Link](https://docs.google.com/presentation/d/1t9K-0OR73WJJfBTiZ8WexCp_GY0HfsMJMqI6e1q9S3A/edit?usp=sharing)

<h2>Electronics Overview</h2>

![image](https://github.com/user-attachments/assets/d4753133-68a3-4934-afa8-c9dc6728d2e6)

<h2>Mechanical Designs</h2>
All components were mounted onto the chassis of the car through 3D prints onto the laser-cut wooden universal frame. The CAD designs of the 3D prints below were made to fit our specific needs and functions. 

**Robot Arm**
<img src="https://github.com/UCSD-ECEMAE-148/winter-2025-final-project-team-1/blob/main/images/arm.png" width="300"/>

**Camera Mount**
<img src="https://github.com/UCSD-ECEMAE-148/winter-2025-final-project-team-1/blob/main/images/camera%20mount%20bottom.png" width= "300"/>
<img src="https://github.com/UCSD-ECEMAE-148/winter-2025-final-project-team-1/blob/main/images/camera%20mount%20top.png" width="300"/>


<h2>Camera Module</h2>

The Oakd camera was needed to identify and lead the car to the precise location to pick up the object. 

A model was trained on Roboflow using the YOLO architecture for object detection. The object used for this project is a red box with a magnet, therefore multiple pictures of the box were uploaded onto Roboflow, annotated, and then trained. The final model (ID: red-box-detection-mae125/2) has a mAP of 99.5%, a precision of 88.7%, and a recall of 100%. These high results ensure accurate detection of the object in question at different angles and environmental factors. 

The model was then deployed into the camera using a Python script (redbox.py). Since the camera is connected to the jetson, depthai and depthai-sdk were used to run the model on jetson while taking the inputs from the camera. 


<h2>Electromagnet Module</h2>

The diagram below outlines the configuration of the circuitry behind the robot's retrieval actuation. A relay sits in series between a battery and magnet, and the relay takes input signals from the Arduino to ultimately open/close the circuit.

![Magnet Circuit!](/images/circuit.png "Arduino and E-Magnet Circuit")

Per Ampere's Law, when current flows through coils of wire, this gives rise to a magnetic field. When this field interacts with an object with a magnetic dipole, attraction or repulsion occurs between them. In fact, the mechanism by which the relay open/closes the circuit actually leverages this to use input current as the determinant for a functional circuit. When the relay closes (and current can reach the electromagnet), then a magnetic field is generated, yielding attraction between the magnet and the object of interest.


Using an arduino presents the unique ability to leverage serial communication and programmatically facilitate the output of digital on/off signals. The functionality of our arduino-magnet scheme fits our project goal well, since  our retrieval robot needs just a simple binary decision as to whether or not to actuate the cascade of events which allows it to pick an object up.

Regarding the implementation of the programmatic control of the magnet, we interfaced a Python script with an Arduino sketch to allow for higher-level control of the Arduino’s output signals. This involved the Serial library from Python, which allowed for headache-free integration between these two scripts. In order to promote communication between these two scripts, the baud rate (communication frequency) between the Python and Arduino sketches, as well as configuring the hardware port in the Jetson that our Arduino occupies. The Python script translated image recognition results from our Roboflow model to dictate digital signals for our Arduino to send.

With more freedom in our project timeline, I imagine that future iterations would involve a more sophisticated casing for the Arduino and Battery on our car. In addition, improved soldering and safety precautions should be made to ensure that wires are securely separated from each other. Nore generic functionality might involve the discretion of using stronger and larger magnets to retrieve the object. This capability would necessitate the categorization of the object we’re trying to recognize, and—-in terms of implementation—-delineation between the logic lines of actuating the magnets of different size and strength.

Gps integration


# Integrating DonkeyCar GPS, Red Box Detection, and Arduino Electromagnet Control

Combining the three separate systems into one unified Python script:

1. **DonkeyCar** – Autonomous driving following a predefined path.
2. **RedBox Detector** (`redbox.py`) – Detects a red box to trigger actions.
3. **Arduino** – Controls an electromagnet (ON/OFF) via serial commands.

## Objective

- Let **DonkeyCar** follow a normal path.
- Once `redbox.py` detects the red box:
  - Switch DonkeyCar to a "return home" path.
  - Send a signal to Arduino to **turn ON** the electromagnet.
- When DonkeyCar reaches the end of the home path:
  - Signal Arduino to **turn OFF** the electromagnet.

## Requirements

- All three programs already exist and are functional individually.
- You can import the red box detection as a function `detect_redbox()`.
- You know how to determine when the car has returned home.
- Arduino is connected via USB (e.g., `/dev/ttyUSB0`) and accepts `ON` / `OFF` commands over serial.
 
# Acknowledgements
_Thank you to Professor Jack Silberman and our TAs Alexander and Winston_


