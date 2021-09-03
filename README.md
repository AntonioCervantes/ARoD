# ARoD - Autonomous Robot of Delivery
ARoD was a project for my Mechanical Engineering senior project. The purpose of this project was to design and build a fully autonomous delivery robot that can deliver food and supplies on the San Jose State University campus. The goal for our team was to have ARoD deliver food from the Student Union to the Martin Luther King Library completely autonomously. We were succussful in completing this goal and a video of the delivery route can be seen in the following video.

https://youtu.be/VCPlvbe8okU

The robot itself was designed and built completely from scratch by a team of four mechanical engineering students. The drive system is a ackermann-based system that features a different gearbox and an ackermann steering mechanism. The drive system chassis is mach made from t-slot extrusions and 3D printed parts. The main body chassis features a secure locking food compartment and housing for electronics and sensors. The main aesthetic to the main body of ARoD is the LED panel which displays eyes giving the robot personality and friendliness. The main body ws built with acrylic plastic and 3D printed parts.

![Chavez Fountain](https://user-images.githubusercontent.com/87390731/132059380-2cf42554-f614-4f79-8340-ac711c8e3d96.jpg)

## Main code loop
The main code can be seen in the graph below. The region colored in red is the food delivery loop, and the blue is the navigation and obstalce avoidance loop. All of the code was written in multiple modules that feature functions for sensors and logical calculations. The [Waypoint_Navigation.py](https://github.com/AntonioCervantes/ARoD/blob/main/Final_code/Waypoint_Navigation.py) is the master code script that is run on ARoD's food delivery process.

![ARoD main code loop](https://user-images.githubusercontent.com/87390731/132056594-9bae8fb3-650e-409b-ad7d-ae9d5efedf79.png)

## Interesting Features
### GUI using GUIZero
We created a graphical user interface to help with testing and remote control of the robot. Using the GUIZero python library this GUI feature buttons to steering, opening and closing the food compartment door, turning on and off the drive motor, and motor/ESC calibration. Code for the GUI can be found in [guizero_gui.py](https://github.com/AntonioCervantes/ARoD/blob/main/Final_code/guizero_gui.py)

![GUI](https://user-images.githubusercontent.com/87390731/132073848-21ffd110-c60f-4251-a31d-9a931b20d81a.JPG)

### Magnetometer Calibration Scipt using MATLAB
The robot uses a magnetometer for heading information, and the sensor we used was the LSM9DS1 from Adafruit. To get usable heading direction information the sensor had to be calibrated for magnetic interferences. We created the [Magnetometer_Calibration.m](https://github.com/AntonioCervantes/ARoD/blob/main/Final_code/Magnetometer_Calibration.m) MATLAB script to read in raw sensor data and calculate the XYZ hard iron offsets. An example of the calibration can be seen in the following graphs.

Uncalibrated
![RPI_uncal_data](https://user-images.githubusercontent.com/87390731/132074464-ea57057e-444b-47e5-b999-e01399e5b364.jpg)

Calibrated
![RPI_cal_data](https://user-images.githubusercontent.com/87390731/132074472-0604ae53-5702-4932-abfc-60e1d607e67a.jpg)
