import os
import cv2 as cv
import numpy as np

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
DIR = r"D:\OpenCV_me\Resources\Faces\train"

# p = []
# for i in os.listdir(DIR):    # --> looping through a folder
#     p.append(i)
#
# print(p)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)


        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
            for(x, y, w, h) in faces_rect:
                faces_region = gray[y:y+h, x:x+w]
                features.append(faces_region)
                labels.append(label)


create_train()
print("--------------------Training Done!----------------------")


# print(f"Length of the features = {len(features)}")
# print(f"Length of the labels = {len(labels)}")
features = np.array(features, dtype="object")
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Training the recognizer on the feature list and labels list
face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")        # opencv allows us to save a model in a yaml.yml file to use it in another file
np.save("features.npy", features)
np.save("labels.npy", labels)