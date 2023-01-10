# store standard pages

from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
import mysql.connector


views = Blueprint('views', __name__)


@views.route('/')
# @login_required
def home():
    # mydb = mysql.connector.connect(host='localhost', user='root', password='0170', database='facedb')
    # cur = mydb.cursor()
    # cur.execute(
    #     "SELECT Student_ID, Last_Name, First_Name, Student_Status FROM class_list where Class_Subject_ID = 'CSC 0312.1' ORDER BY Last_Name;")
    # output = cur.fetchall()
    # cur.close()

    # StdID = []
    # Lst_Name = []
    # Frst_Name = []
    # Std_Status = []

    # for line in output:
    #     print(line)
    #     field = list(line)
    #     StdID.append(field[0])
    #     Lst_Name.append(field[1])
    #     Frst_Name.append(field[2])
    #     Std_Status.append(field[3])

    # return render_template("home.html", len=len(StdID), stdID=StdID, lstName=Lst_Name, frstName=Frst_Name,
    #                        StdStatus=Std_Status, user=current_user)
    return render_template("home.html")