import cv2

# Read the image
image = cv2.imread("D:\\Desktop\\photos\\1.jpg")

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()