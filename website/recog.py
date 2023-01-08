import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from flask import Flask, render_template, Response, Blueprint
import csv
import mysql.connector

# app = Flask(__name__)
recog = Blueprint('recog', __name__)

stdNames = []
encodeStdKnown = []
path = 'image'
myList = os.listdir(path)

for cl in myList:
    stdNames.append(os.path.splitext(cl)[0])
print(stdNames)

def findEncodings():
    for image in os.listdir('image'):
        face_image = face_recognition.load_image_file(f"image/{image}") # TODO Make string only get before comma (,) (BARRIOS, Gabriel Nicoh)
        face_encoding = face_recognition.face_encodings(face_image)[0]
        encodeStdKnown.append(face_encoding)

def Attendance(name):
    with open('website/attendance.csv', 'r+') as f:
        AttendanceList = []
        myDataList = f.readlines()
        for line in myDataList:
            entry = line.split(',')
            AttendanceList.append(entry[1])
        if name not in AttendanceList:
            now = datetime.now()
            dtString = now.strftime('%H:%M')
            f.writelines(f'\n{len(AttendanceList)},{name},{dtString}')

logStatus = {}
nameList = []
def Logging(name):
    with open('website/logging.csv', 'r+') as f:
        # print(f'INITIAL: {logStatus}')
        myDataList = f.readlines()
        status = ''
        for line in myDataList:
            entry = line.rstrip('\n').split(',')
            # print(f'ENTRY: {entry}')
            nameList.append(entry[1])
            logStatus[entry[1]] = entry[3]

        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%H:%M:%S')
            status = 'IN'
            logStatus[name] = status
            f.writelines(f'\n{len(myDataList)},{name},{time},{status}')

        if name in nameList:
            if logStatus[name] == 'IN':
                now = datetime.now()
                time = now.strftime('%H:%M:%S')
                status = 'OUT'
                logStatus[name] = status
                f.writelines(f'\n{len(myDataList)},{name},{time},{status}')
            elif logStatus[name] == 'OUT':
                now = datetime.now()
                time = now.strftime('%H:%M:%S')
                status = 'IN'
                logStatus[name] = status
                f.writelines(f'\n{len(myDataList)},{name},{time},{status}')

findEncodings()
print('Encoding Complete')

# facial recognition
def main_face_recog():
    current_frame = True
    vid = cv2.VideoCapture(0)

    if not vid.isOpened():
        print('ERROR! No video source found...')

    timer = 0
    found = False
    while True:
        ret, img = vid.read()

        if current_frame:
            imgS = cv2.resize(img, (0, 0), fx= 0.25, fy=0.25)
            rgb_imgS = imgS[:, :, ::-1]

            # find all the faces and face encodings in current frame of video
            facesCurFrame = face_recognition.face_locations(rgb_imgS)
            encodesCurFrame = face_recognition.face_encodings(rgb_imgS, facesCurFrame) # TODO this is what causes lag

            if not facesCurFrame: # if there are no faces restart the timer
                timer = 0
                found = False

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
                if timer == 6: # if lasts for 6 seconds log
                    Logging(name)
                    Attendance(name)
                    found = True
                
                detected_faces.append(f'{name}')

        current_frame = not current_frame

        # display results
        for (top, right, bottom, left), name in zip(facesCurFrame, detected_faces):
            # scale face locations 5 because we shrunk the image to 1/5, 4 1/4
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            b,g,r = 0,0,0
            msgText = ''

            # create a frame with name
            if found:
                b,g,r=0,255,0 # green
                msgText = name
            elif name is not 'Unknown Student':
                b,g,r=255,0,0 # blue
                msgText = 'Detecting...'
            else:
                b,g,r=0,0,255# red
                msgText = name
            
            cv2.rectangle(img, (left, top), (right, bottom), (b,g,r), 2)
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (b,g,r), cv2.FILLED)
            cv2.putText(img, msgText, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)


        ret, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

@recog.route('/face-recog')
def index():
    return render_template('face-recog.html')

@recog.route('/video_feed')
def video_feed():
    return Response(main_face_recog(), mimetype='multipart/x-mixed-replace; boundary=frame')
@recog.route('/view')
def csv_database():
    mydb = mysql.connector.connect(host='localhost', user='root', password='0170', database='facedb')
    print('database connected')
    cursor = mydb.cursor()
    csv_data = csv.reader(open('website/attendance.csv'))
    next(csv_data)
    for row in csv_data:
        cursor.execute('INSERT INTO attendancesubject (id,atdc_name,atdc_date) VALUES(%s,%s,%s)', row)
        print(row)

    mydb.commit()
    cursor.close()

    cursor = mydb.cursor()
    csv_data = csv.reader(open('website/logging.csv'))
    next(csv_data)
    for row in csv_data:
        cursor.execute('INSERT INTO logsubject (id,log_name,log_time,log_status) VALUES(%s,%s,%s,%s)', row)
        print(row)

    mydb.commit()
    cursor.close()
    return render_template('view.html')

if __name__=='__main__':
    recog.run(debug=True)


# cv2.imshow('Webcam', img)

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# vid.release()
# cv2.destroyAllWindows()