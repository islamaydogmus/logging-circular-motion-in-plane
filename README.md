# Simple apparatus for logging circular motion in plane

## Videos

### Demo
https://user-images.githubusercontent.com/67843280/159893979-5a88dbd7-75bc-46be-9468-ac73c148431d.mp4

### Demo 2

https://user-images.githubusercontent.com/67843280/159894912-db4d0244-fb66-4253-a954-081fc0560e12.mp4

### Projection Feature

https://user-images.githubusercontent.com/67843280/159894146-efd4f6cf-0bc8-4de6-a19a-19ebc268be3a.mp4




## Introduction
 Potentiometers are resistive displacement sensing elements. They work according to simple voltage dividing principle. It divides its input voltage to output voltage according to position of your adjustable armature.
<p align="center">
  <img src="https://github.com/islamaydogmus/logging-circular-motion-in-plane/blob/main/README_images/Pot_image.png" />
</p>
   
 In this assignment, we’ll use 2 kinds of potentiometers. One is linear, other is rotary pot. We’ll put these pots together to construct an armature structure which we can move in plane with 2 degrees of freedom (there might be some constrains). System structure approximately looks like this Figure 1.
 
 <p align="center">
  <img src="https://github.com/islamaydogmus/logging-circular-motion-in-plane/blob/main/README_images/Diagram.png" />
</p>
 
  
Vin is 5V output of Arduino. Actually, in this configuration there is no need for voltage mapping since Arduino can read in 0-5V range. Arduinos are relatively expensive circuitries so we can map it to 1-4V if we need to. But we'll not bother to do for this time.


### Interface Circuit

It’s very easy circuitry. Vlin and Vrot will change between 0 and 5 volt linearly. 
<p align="center">
  <img src="https://github.com/islamaydogmus/logging-circular-motion-in-plane/blob/main/README_images/circuitry.png" />
</p>
Since we can supply Vin from Arduino, there will be no need for external voltage source.

### Configurations
  
You should check which port you connected your Arduino. Then change 'port' variable to that port. Measure the length of your linear pot and change 'LINLENGTH' parameter to measured length in centimeters. There is probably also a deadzone between origin and 0Ω point in your linear potentiometer so you can measure and add that value to 'DEADZONE' variable.


