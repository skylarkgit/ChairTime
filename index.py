# Import the required packages
import cv2
import time
import imutils
 
# Initialize the HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Loop over the image paths
while True:
    # Read the image and resize it.
    image = cv2.imread('test-yes.jpg')
    image = imutils.resize(image, width=min(400, image.shape[1]))
    
    # Detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
        padding=(8, 8), scale=1.05)
    
    # Draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
    # Show the output image
    cv2.imshow("Detect  People", image)
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()