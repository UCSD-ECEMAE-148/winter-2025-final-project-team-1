# winter-2025-final-project-team-1
148-winter-2025-final-project-team-1 created by GitHub Classroom

<h2>Electromagnet Module</h2>

The diagram below outlines the configuration of the circuitry behind the robot's retrieval actuation. A relay sits in series between a battery and magnet, and the relay takes input signals from the Arduino to ultimately open/close the circuit.

![Magnet Circuit!](/images/circuit.png "Arduino and E-Magnet Circuit")

Per Ampere's Law, when current flows through coils of wire, this gives rise to a magnetic field. When this field interacts with an object with a magnetic dipole, attraction or repulsion occurs between them. In fact, the mechanism by which the relay open/closes the circuit actually leverages this to use input current as the determinant for a functional circuit. When the relay closes (and current can reach the electromagnet), then a magnetic field is generated, yielding attraction between the magnet and the object of interest.


Using an arduino presents the unique ability to leverage serial communication and programmatically facilitate the output of digital on/off signals. The functionality of our arduino-magnet scheme fits our project goal well, since  our retrieval robot needs just a simple binary decision as to whether or not to actuate the cascade of events which allows it to pick an object up.

Regarding the implementation of the programmatic control of the magnet, we interfaced a Python script with an Arduino sketch to allow for higher-level control of the Arduino’s output signals. This involved the Serial library from Python, which allowed for headache-free integration between these two scripts. In order to promote communication between these two scripts, the baud rate (communication frequency) between the Python and Arduino sketches, as well as configuring the hardware port in the Jetson that our Arduino occupies. The Python script translated image recognition results from our Roboflow model to dictate digital signals for our Arduino to send.

With more freedom in our project timeline, I imagine that future iterations would involve a more sophisticated casing for the Arduino and Battery on our car. In addition, improved soldering and safety precautions should be made to ensure that wires are securely separated from each other. Nore generic functionality might involve the discretion of using stronger and larger magnets to retrieve the object. This capability would necessitate the categorization of the object we’re trying to recognize, and—-in terms of implementation—-delineation between the logic lines of actuating the magnets of different size and strength.

Gps integration


# Integrating DonkeyCar GPS, Red Box Detection, and Arduino Electromagnet Control

This guide combines three separate systems into one unified Python script:

1. **DonkeyCar** – Autonomous driving following a predefined path.
2. **RedBox Detector** (`redbox.py`) – Detects a red box to trigger actions.
3. **Arduino** – Controls an electromagnet (ON/OFF) via serial commands.

---

## Objective

- Let **DonkeyCar** follow a normal path.
- Once `redbox.py` detects the red box:
  - Switch DonkeyCar to a "return home" path.
  - Send a signal to Arduino to **turn ON** the electromagnet.
- When DonkeyCar reaches the end of the home path:
  - Signal Arduino to **turn OFF** the electromagnet.

---

## Requirements

- All three programs already exist and are functional individually.
- You can import the red box detection as a function `detect_redbox()`.
- You know how to determine when the car has returned home.
- Arduino is connected via USB (e.g., `/dev/ttyUSB0`) and accepts `ON` / `OFF` commands over serial.

