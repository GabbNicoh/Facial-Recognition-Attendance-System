import cv2
import numpy as np
import face_recognition
import os

images = []
stdNames = []
encodeListKnown = []
path = 'image'
myList = os.listdir(path)
process_current_frame = True

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    stdNames.append(os.path.splitext(cl)[0])
print(stdNames)

def findEncodings():
    for image in os.listdir('image'):
        face_image = face_recognition.load_image_file(f"image/{image}")
        face_encoding = face_recognition.face_encodings(face_image)[0]
        encodeListKnown.append(face_encoding)

findEncodings()
print('Encoding Complete')

# facial recognition
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('ERROR! No video source found...')

while True:
    success, img = cap.read()
    
    if process_current_frame:
        imgS = cv2.resize(img, (0, 0), fx= 0.25, fy=0.25)
        rgb_imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB) # TODO: change to gray to reduce lag
        
        # find all the faces and face encodings in current frame of video
        facesCurFrame = face_recognition.face_locations(rgb_imgS) 
        encodesCurFrame = face_recognition.face_encodings(rgb_imgS, facesCurFrame) # TODO: this is what causes lag

        detected_faces = []
        for encodeFace in encodesCurFrame:
            # see if face is a match for known faces
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            name = 'Unknown'

            # Calculate shortest distance from face
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            # checks if face are a match
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = stdNames[matchIndex]
            detected_faces.append(f'{name}')

    process_current_frame = not process_current_frame

    # display results
    for (top, right, bottom, left), name in zip(facesCurFrame, detected_faces):
        # scale face locations
        top,right,bottom,left = top * 4, right * 4, bottom * 4, left * 4

        # create a frame with name
        if name is not 'Unknown':
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)

        else:
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

    cv2.imshow('Webcam', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
