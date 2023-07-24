import cv2
import os
import pickle
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://real-time-face-detection-fd855-default-rtdb.firebaseio.com/",
    'storageBucket':"real-time-face-detection-fd855.appspot.com"
})

# IMPORTING STUDENT IMAGES
folderPath = "Images"
pathList = os.listdir(folderPath)
# print(pathList)
studentIDs = []
imgList = []
# print(modePathList)

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    print(path)
    print(os.path.splitext(path)[0]) # Gives first image
    studentIDs.append(os.path.splitext(path)[0])

    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

print(len(imgList))
print(studentIDs)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding started...")
encodeListKnown = findEncodings(imgList)
# print(encodeListKnown) // THIS IS THE MAIN ARRAY OF DIFFERENT FACE PIXELS
print("Encoding complete")

encodeListKnownwithIds = [encodeListKnown, studentIDs]

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownwithIds, file)
file.close()
print("File Saved")


