import cv2

# Read the image
image = cv2.imread("D:\\Desktop\\photos\\1.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()