import cv2

# Load the image
image = cv2.imread('watch.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the watch cascade classifier
watch_cascade = cv2.CascadeClassifier('watch_cascade.xml')

# Detect watches in the image
watches = watch_cascade.detectMultiScale(gray)

# Draw bounding boxes around the detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, 'Watch', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the result
cv2.imshow('Object Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
