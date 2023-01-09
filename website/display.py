import os
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='0170', database='facedb')

cursor = mydb.cursor()
cursor.execute("SELECT * FROM class_list;")
result = cursor.fetchall()
print(result)
mydb.commit()
cursor.close()

df = pd.DataFrame()
for x in result:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html('templates/shows.html')
