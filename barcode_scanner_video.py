# Importing the required packages and libraries
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import argparse
import cv2
import datetime
import time

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv", help="path to output CSV File containing barcodes")
args = vars(ap.parse_args())

# Initialize the VideoStream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()     # src=0 tells the imutils library to search for the primary built-in camera connected directly to your computer's motherboard or USB port - which is almost always the laptop's webcam
time.sleep(2.0)     # It pauses the execution for 2 seconds allowing the laptop's camera sensor to warm up


# open the output CSV file for writing and initialize the set of barcodes found thus far
csv = open(args["output"], "w")
found = set()   # This set will contain unique barcodes while preventing duplicates

# Loop over frames from the video stream
while True:
    # grab a frame from the threaded video stream and resize it to have a maximum width of 400 pixels 
    frame = vs.read()
    # frame = imutils.resize(frame, width=400)
    
    # Find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    
    # loop over detected barcodes 
    for barcode in barcodes:
        # Extract the bouding box location of the barcode and draw the bouding box surrounding 
        # the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        # the barcode data is a bytes object so if we want to draw it 
        # on our image we would have to convert it into string first
        bcData = barcode.data.decode("utf-8")
        bcType = barcode.type
        
        # draw the barcode data and barcode type on the image 
        text = "{} [{}]".format(bcData, bcType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # If the barcode data is not present in our csv file currently, 
        # write timestamp + barcode data to the disk and update the set 
        if bcData not in found:
            csv.write("{} {}\n".format(datetime.datetime.now(), bcData))
            csv.flush()
            found.add(bcData)
            
    # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
        
    # If the key "q" was pressed, break from the loop
    if key == ord("q"):
        break
    
    
# close the output CSV file and do a bit of cleanup
print("[INFO] cleaning up...") 
csv.close()
cv2.destroyAllWindows()
vs.stop()
        
    