import cv2

# Read the image
image = cv2.imread("D:\\Desktop\\photos\\1.jpg")

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()