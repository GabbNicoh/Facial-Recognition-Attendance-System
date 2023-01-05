from datetime import datetime
import threading

# TODO: INCREMENT FACE TO REACH A PONIT IF POINT REACHED THEN LOG

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

# Attendance('Test')

logStatus = {}
def Logging(name):
    with open('logging.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        status = ''
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            
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
                nameList.remove(name)
                f.writelines(f'\n{name},{time},{status}')

        print(f'DICTIONARY: {logStatus}')
        print(f'Namelist: {nameList}')
            
Logging('YourMom')

event = threading.Event()
event.wait(3)

Logging('JackDaniaels')
Logging('YourMom')