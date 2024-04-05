# CSE360 Lab 8 - By: Scarlet - Fri Mar 29 2024

import sensor, image, time
import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time # Import module for tracking elapsed time

nesflip = False

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(nesflip) # Flips the image vertically
sensor.set_hmirror(nesflip) # Mirrors the image horizontally
sensor.skip_frames(time = 2000)

threshBall = (38, 76, -19, 24, 24, 60)

ledRed = pyb.LED(1) # Initiates the red led
ledGreen = pyb.LED(2) # Initiates the green led

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([threshBall], area_threshold=2500, merge=True)
    for blob in blobs:
        # Draw a rectangle where the blob was found
        img.draw_rectangle(blob.rect(), color=(0,255,0))
        wid = blob.rect()[2]
        hite = blob.rect()[3]

        print(str(wid) + "x" + str(hite))
        # Draw a cross in the middle of the blob
        img.draw_cross(blob.cx(), blob.cy(), color=(0,255,0))
        print(str(blob.cx()) + ", " + str(blob.cy()))

    # Turn on green LED if a blob was found
    if len(blobs) > 0:
        ledGreen.on()
        ledRed.off()
    else:
        # Turn the red LED on if no blob was found
        ledGreen.off()
        ledRed.on()
    pyb.delay(50) # Pauses the execution for 50ms
    print(clock.fps())
