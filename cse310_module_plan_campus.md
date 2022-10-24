# Overview

A Python program that will take feed from your camera and recognize hand gestures.

The hand signs it can recognize are: 
- open palm (high five)
- closed fist
- peace sign (this will maximize the active window)
- four fingers up, close together (turn volume down)
- four fingers up, spread apart (turn volume up)


[Software Demo Video](http://youtu.be/zLZY28peYC8?hd=1)

# Development Environment
I used Python and a hand recognition library by cvzone. 
To trigger computer functions, I used pynput to simulate keyboard shortcuts


# Useful Websites

* [hand detection tutorial](https://aihubprojects.com/hand-detection-gesture-recognition-opencv-python/)
* [cvzone documentation](https://github.com/cvzone/cvzone)

# Future Work

- add a debouncer for maximizing the window (right now it just uses a timeout)
- add more hand signs