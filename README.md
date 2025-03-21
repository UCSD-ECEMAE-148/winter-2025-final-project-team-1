# winter-2025-final-project-team-1
148-winter-2025-final-project-team-1 created by GitHub Classroom

<h2>Electromagnet Module</h2>

but the diagram here outlines a pretty simple configuration where a relay sits in series between a battery and magnet, and the relay takes input signals from the arduino to ultimately open/close the circuit.



<theory of how current actuates magnetic field for magnet, and identical phenomenon takes place within the relay to open/close the circuit>



when you have coils of wire, sending current through them gives rise to a magnetic field. when interacting with an object with a magnetic dipole, we have attraction/repulsion between them. the mechanism by which the relay open/closes the circuit actually leverages this to use input current as the determinant for a functional circuit.



using an arduino presents the unique ability to leverage serial communication and programmatically facilitate the output of digital on/off signals. the functionality of our arduino-magnet scheme fits our project goal well, since  our retrieval robot needs just a simple binary decision as to whether or not to actuate the cascade of events which allows it to pick an object up.



regarding the implementation of the programmatic control of the magnet, we interfaced a python script with an arduino sketch to allow for higher-level control the arduino’s output signals. this involved the Serial library from python, which allowed for headache-free integration between these two scripts. syncing the baud rate (communication frequency) between the python and arduino sketches, as well as configuring the hardware port in the jetson that our arduino occupies, the python script translated image recognition results from our roboflow model to digital signals for our arduino.



with more freedom in our project timeline, i imagine that future iterations would involve a more sophisticated casing for the arduino and battery on our car. in addition, improved soldering and safety precautions should be made to ensure that wires are securely separated from each other (nicer job with wiring tape). more generic functionality might involve the discretion of using stronger and larger magnets to retrieve the object— this would necessitate the categorization of the object we’re trying to recognize, and—in terms of implementation— delineation between the logic lines of actuating the magnets of different size/strength
