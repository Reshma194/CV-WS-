import cv2 as cv
# Function to rescale frame
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)  # Define the dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Read the image
img = cv.imread(r'C:\Users\DELL\Desktop\ghj.jpeg')

# Ensure the image is loaded properly
if img is None:
    print("Error: Image not found!")
else:
    # Resize the image using the rescaleFrame function
    resized_image = rescaleFrame(img)

    # Display the original and resized images
    cv.imshow('Original Image', img)
    cv.imshow('Resized Image', resized_image)

    # Wait for a key press and close all windows
    cv.waitKey(0)
    cv.destroyAllWindows()
