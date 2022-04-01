# Invisibility_Cloak

## If it looks fun for a **day's** project :D

The code break down is pretty simple:

1. Read the background first using Opencv's cap.read() and store it in a variable.
2. Start capturing the video and use HSV color coding instead of BGR as it has more pallete of colors pre-defined.
3. Define lower and upper bounds of your choice of color(mine was blue). and mask using InRange fcn which makes any value in that range 255.
4. **Convert any 255 values pixel to background pixel hence, done !**

![invisible](https://user-images.githubusercontent.com/60159274/161189419-7e91547e-d21a-4956-ba23-b1401f59a071.gif)
