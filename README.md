# Overview

A Python program that will take feed from your camera and recognize hand gestures.

The hand signs it can recognize are: 
- open palm (high five)
- closed fist
- peace sign (toggle lights on/off)
- four fingers up, close together (turn brightness down)
- four fingers up, spread apart (turn brightness up)


[Software Demo Video](http://youtu.be/u9Mpyg6Jm1c?hd=1)

# Development Environment
I used Python and a hand recognition library by cvzone.

Philips hue api works with my philips hue lights and bridge


# Useful Websites

* [hand detection tutorial](https://aihubprojects.com/hand-detection-gesture-recognition-opencv-python/)
* [cvzone documentation](https://github.com/cvzone/cvzone)
* [philips hue developer docs](https://developers.meethue.com/)
# Future Work

- add a debouncer for toggle (right now it just uses a timeout)
- add more hand signs
- control color too
- practice using more light zones once I get more lights to work with