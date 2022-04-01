# Invisibility_Cloak

## If it looks fun for a **day's** project, Forget it, coz its an **hour** project :D

The code break down is pretty simple:

1. Read the background first using Opencv's cap.read() and store it in a variable.
2. Start capturing the video and use HSV color coding instead of BGR as it has more pallete of colors pre-defined.
3. Define lower and upper bounds of your choice of color(mine was blue). and mask using InRange fcn which makes any value in that range 255.
4. **Convert any 255 values pixel to background pixel hence, done !**

![My Cloak](https://media.giphy.com/media/M9CqcbNWeePnpKtVb8/giphy.gif)


