## Simple apparatus for logging circular motion in plane

 Potentiometers are resistive displacement sensing elements. They work according to simple voltage dividing principle. It divides its input voltage to output voltage according to position of your adjustable armature.
<p align="center">
  <img src="https://github.com/islamaydogmus/logging-circular-motion-in-plane/blob/main/README_images/Pot_image.png" />
</p>
   
 In this assignment, we’ll use 2 kinds of potentiometers. One is linear, other is rotary pot. We’ll put these pots together to construct an armature structure which we can move in plane with 2 degrees of freedom (there might be some constrains). System structure approximately looks like this Figure 1.
 
 <p align="center">
  <img src="https://github.com/islamaydogmus/logging-circular-motion-in-plane/blob/main/README_images/Diagram.png" />
</p>
 
  
Vin is 5V output of Arduino. Actually, in this configuration there is no need for voltage mapping since Arduino can read in 0-5V range but Arduinos are relatively expensive circuitries so we can map it to 1-4V if we need to. 
