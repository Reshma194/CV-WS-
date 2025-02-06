import cv2 as cv

# Create a VideoCapture object and read from the video file
capture = cv.VideoCapture(r'C:\Users\DELL\Desktop\1182756-hd_1920_1080_25fps.mp4')

while True:
    # Read the frame
    isTrue, frame = capture.read()
    
    # Break the loop if no frame is captured (end of video)
    if not isTrue:
        break
    
    # Display the frame
    cv.imshow('Video', frame)
    
    # Exit the video display when 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object and close windows
capture.release()
cv.destroyAllWindows()
