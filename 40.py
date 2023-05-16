import cv2

# Load the image
image = cv2.imread('watch.jpg')

# Draw a rectangle on the image
start_point = (100, 100)
end_point = (300, 400)
color = (0, 255, 0)
thickness = 2
cv2.rectangle(image, start_point, end_point, color, thickness)

# Extract the object within the rectangle
roi = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]

# Display the results
cv2.imshow('Image with Rectangle', image)
cv2.imshow('Extracted Object', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
