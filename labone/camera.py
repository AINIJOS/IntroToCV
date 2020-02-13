import cv2

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))

cap = cv2.VideoCapture(0)
while True:
    # Capture a frame
    flag, frame = cap.read()

    current = cv2.blur(frame, (5, 5))
    previous = cv2.blur(frame, (5, 5))
    difference = cv2.absdiff(current, previous)

    frame2 = frame.copy()
    frame2[(frame[..., 1] < 150) | (frame[..., 2] < 185)] = 0 # Цвет кожи 

    cv2.imshow('window_a', frame2)
    cv2.imshow('window_b', frame)

    previous = current



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()