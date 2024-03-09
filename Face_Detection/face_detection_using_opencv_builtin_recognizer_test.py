import cv2 as cv
import numpy as np

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# features = np.load("features.npy")
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# Testing
img = cv.imread(r"D:\OpenCV_me\Resources\Faces\val\madonna\3.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("person", gray)

# detect face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_region = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_region)
    print(f"Label = {people[label]} with a confidence of {confidence}")

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=1)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow("Detected Faces", img)



cv.waitKey(0)