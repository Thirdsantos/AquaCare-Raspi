import cv2
from pathlib import Path

dir = Path("images") / "sample.jpg"

img = cv2.imread(dir)

cap = cv2.VideoCapture(0)

while True:

  ret, frame = cap.read()

  if not ret:
    break

  cv2.imshow("webcam", frame)

cap.release()
cv2.destroyAllWindows()