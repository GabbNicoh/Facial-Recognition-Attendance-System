# Facial Recognition Attendance System
Project for Software Engineering CSC 0313.

Detect and recognize a student's face using Python and OpenCV. After recognizing the student, it logs the time and places it into an excel file.

- `Facial Detection` - The ability of the program to 'detect' faces.

- `Facial Recognition` - The ability of the program to 'identify' whose faces are shown.

[![Documentation Status](https://readthedocs.org/projects/face-recognition/badge/?version=latest)](http://face-recognition.readthedocs.io/en/latest/?badge=latest)

## Similar Studies
### Geitgey, Adam 
- [Medium Article (2016)](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)
- [Face Recognition](https://github.com/ageitgey/face_recognition)

`Add description and how they did Facial Detection and Recognition`

### Murtaza's Workshop
- [Youtube (2020)](https://www.youtube.com/watch?v=sz25xxF_AVE)

### Pysource
- [Youtube (2021)](https://www.youtube.com/watch?v=5yPeKQzCPdI)

### I know python
- [Youtube (2022)](https://www.youtube.com/watch?v=A6464U4bPPQ)

## Goals
- [ ] Facial Detection & Recognition System
- [ ] Train AI to be accurate? (not sure if modules are allowed)
- [ ] Publish time, date and name of student on to an excel file 
- [ ] Logs

### Additionals
- Add delay for 5 minutes every recognized students
- How accurate is the system
- UI for the facial recognition and menu 
- Student Attendance Statistics (DATABASE)
  - Records a class' number of present, lates and absent

## Notes
- Tilted Head
- Low Brightness
- With Face Mask

## Installation
### Requirements
- Python 3.x+ (3.7)
> pip install cmake
>     if error need C and C++ compilers to install Dlib (We can use Visual Studio 2019)

> pip install dlib==19.22

> pip install opencv-python

> pip install face_recognition

- Database MySQL Driver
> pip install mysql-connector-python

- Web
> pip install flask

> pip install flask-login

> pip install flask-sqlalchemy

## Classifer & Algorithm
https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

https://face-recognition.readthedocs.io/en/latest/usage.html

https://github.com/indently/webcam_face_recognition/blob/master/recognition.py

https://www.youtube.com/watch?v=tl2eEBFEHqM

https://www.youtube.com/watch?v=sz25xxF_AVE

https://www.youtube.com/watch?v=QSTnwsZj2yc

https://youtu.be/dam0GPOAvVI (FLASK)

https://youtu.be/iM3kjbbKHQU (TKINTER)

## Steps
- Encode
- Detect
- Compare Faces
- Log

## Tips
- Store encodings in xml file to save encoding time
- Pass image as gray scale and small size by using opencv
- Run on separate thread
- ADD PROGRESS BAR
- FLASK for WEB FRAMEWORK
  - Initialize
  - Routes
  - Jinja Templating Language & HTML Templates
  - Bootstrap (CSS framework) (TKinter for GUI)
  - 