import cv2

# Read the image
image = cv2.imread("D:\\Desktop\\photos\\1.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the original image and edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()