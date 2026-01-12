from picamera2 import Picamera2
import os
import time
import RPi.GPIO as GPIO
import cv2

def capture_image():
    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start()
    time.sleep(2)


    # This returns a NumPy array (raw RGB pixel data)
    image_array = picam2.capture_array()
    # Convert NumPy array to JPEG bytes
    success, buffer = cv2.imencode(".jpg", image_array)
    if success:
        image_bytes = buffer.tobytes()  # This is raw JPEG file data
        return image_bytes
    else:
        return None


