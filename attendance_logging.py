from datetime import datetime

def Attendance(name):
    with open('attendance.csv', 'r+') as f:
        # reads
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0]) # splits and reads the name and adds it to list
        # writes
        if name not in nameList: # if name is not in list add it with time
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

Attendance('Test')

def Logging(name):
    with open('logging.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
        isIn = False