import numpy as np
import cv2

cap = cv2.VideoCapture(0)   #use webcam number 1

while True:
    ret, frame = cap.read()         #capture the frame

    width = int(cap.get(3))         #see doc
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)                                                # resize to 1/4th the size

    image[:height // 2, :width // 2] = smaller_frame                                                        # paste smaller frames in top left
    image[height // 2:, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)                        # paste smaller frames in bottom left and rotate
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)                        # paste smaller frames in top right and rotate
    image[height // 2:, width // 2:] = cv2.flip(smaller_frame, flipCode = 1)                                # paste smaller frames in bottom right and flip mirror



    cv2.imshow('frame', image)      #show frame and title frame

    if cv2.waitKey(1) == ord('q'):  # after 1 milisecond check if q is pressed and quit
        break

cap.release()                       #release webcam or other videocapture for use elsewhere
cv2.destoyAllWindows


