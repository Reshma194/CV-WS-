import cv2 as cv
# Function to rescale frame
def rescaleFrame(frame, scale=.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)  # Define the dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# Capture video
capture = cv.VideoCapture(r'C:\Users\DELL\Desktop\1182756-hd_1920_1080_25fps.mp4')
while True:
    # Read the frame
    isTrue, frame = capture.read()
    # Break the loop if no frame is captured (end of video)
    if not isTrue:
        break
    # Rescale the frame
    frame_resized = rescaleFrame(frame)
    # Display the original and resized frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    # Exit the video display when 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
# Release the video capture object and close windows
capture.release()
cv.destroyAllWindows()
