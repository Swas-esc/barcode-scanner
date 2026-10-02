# Importing the required packages
from pyzbar import pyzbar
import argparse
import cv2

# Construct the Argument Parser and parse the arguments 
ap = argparse.ArgumentParser()  # Creates an object
ap.add_argument("-i", "--image", required=True, help="Path the image file")
args = vars(ap.parse_args())    # parse_args parses the command line arguments and vars function converts them to Standard Python Dictionary for easy access

# load the input image
image = cv2.imread(args["image"])

# Find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(image)

# loop over the detected barcodes
for barcode in barcodes:
    # extract the bounding box location of barcode and draw the bounding box surrounding barcode in the image
    (x, y, w, h) = barcode.rect     # Tuple Unpacking - stores the location (x, y) and the width and height in pixels (w, h)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)       
    
    # the barcode data is a bytes object so if we want to draw it on our 
    # output image, we need to convert it in string first
    bcData = barcode.data.decode("utf-8")   # Convert it to utf-8 encoding string 
    bcType = barcode.type                   # Store the type of barcode in bcType
    
    # draw the barcode data and barcode type on the image
    text = "{} [{}]".format(bcData, bcType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # print the barcode type and data to the terminal
    print("[INFO] Found {} barcode: {}".format(bcType, bcData))
    
# Show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)