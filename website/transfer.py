import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='0170', database='facedb')
print ('database connected')
# FOR ATTENDANCE
cursor = mydb.cursor()
csv_data = csv.reader(open('attendance.csv'))

for row in csv_data:
    cursor.execute('INSERT INTO attendancesubject (id,atdc_name,atdc_date) VALUES(%s,%s,%s)', row)
    print(row)

mydb.commit()
cursor.close()
# FOR LOGS
cursor = mydb.cursor()
csv_data = csv.reader(open('logging.csv'))

for row in csv_data:
    cursor.execute('INSERT INTO logsubject (id,log_name,log_time,log_status) VALUES(%s,%s,%s,%s)', row)
    print(row)

mydb.commit()
cursor.close()
print("DONE")