import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


stdNames = []
encodeStdKnown = []
path = 'image'
myList = os.listdir(path)
current_frame = True

for cl in myList:
    stdNames.append(os.path.splitext(cl)[0])
print(stdNames)

def findEncodings():
    for image in os.listdir('image'):
        face_image = face_recognition.load_image_file(f"image/{image}") # TODO Make string only get before comma (,) (BARRIOS, Gabriel Nicoh)
        face_encoding = face_recognition.face_encodings(face_image)[0]
        encodeStdKnown.append(face_encoding)

def Attendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M')
            f.writelines(f'\n{name},{dtString}')

logStatus = {}
nameList = []
def Logging(name):
    with open('logging.csv', 'r+') as f:
        # print(f'INITIAL: {logStatus}')
        myDataList = f.readlines()
        status = ''
        for line in myDataList:
            entry = line.rstrip('\n').split(',')
            # print(f'ENTRY: {entry}')
            nameList.append(entry[0])
            logStatus[entry[0]] = entry[2]
            
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%H:%M:%S')
            status = 'IN'
            logStatus[name] = status
            f.writelines(f'\n{name},{time},{status}')
        
        if name in nameList:
            if logStatus[name] == 'IN': 
                now = datetime.now()
                time = now.strftime('%H:%M:%S')
                status = 'OUT'
                logStatus[name] = status
                f.writelines(f'\n{name},{time},{status}')
            elif logStatus[name] == 'OUT':
                now = datetime.now()
                time = now.strftime('%H:%M:%S')
                status = 'IN'
                logStatus[name] = status
                f.writelines(f'\n{name},{time},{status}')

        # print(f'OUTPUT: {logStatus}')

findEncodings()
print('Encoding Complete')

# facial recognition
vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print('ERROR! No video source found...')

timer = 0
while True:
    ret, img = vid.read()
    
    if current_frame:
        imgS = cv2.resize(img, (0, 0), fx= 0.25, fy=0.25)
        rgb_imgS = imgS[:, :, ::-1]

        # find all the faces and face encodings in current frame of video
        facesCurFrame = face_recognition.face_locations(rgb_imgS) # TODO TRY REINSTALLING DLIB WITH CUDA DRIVERS FOR THIS
        encodesCurFrame = face_recognition.face_encodings(rgb_imgS, facesCurFrame) # TODO this is what causes lag
        
        if not facesCurFrame: # if there are no faces restart the timer
            timer = 0

        detected_faces = []
        for encodeFace in encodesCurFrame:
            # see if face is a match for known faces
            matches = face_recognition.compare_faces(encodeStdKnown, encodeFace)
            name = 'Unknown Student'

            # Calculate shortest distance from face
            faceDis = face_recognition.face_distance(encodeStdKnown, encodeFace)

            # checks if face are a match
            isMatch = np.argmin(faceDis)
            if matches[isMatch]:
                name = stdNames[isMatch]

            timer += 1
            print(f'TIMER: {timer}') 
            # TODO make it so if it is done turn green
            if timer >= 7:
                Logging(name)
                timer = 0

            Attendance(name)
            detected_faces.append(f'{name}')

    current_frame = not current_frame

    # display results
    for (top, right, bottom, left), name in zip(facesCurFrame, detected_faces):
        # scale face locations 5 because we shrunk the image to 1/5, 4 1/4
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # create a frame with name
        if name is not 'Unknown Student':
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2) # draw box around face
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED) # draw label with name below
        else:
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

    cv2.imshow('Webcam', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
