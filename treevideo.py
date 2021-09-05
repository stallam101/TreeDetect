import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier("cascade(1).xml")

cap = cv2.VideoCapture('trees.mp4')

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
      faces = face_cascade.detectMultiScale(frame, 1.01, 7)
      for (x,y,w,h) in faces:
          frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
