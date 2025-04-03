from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import random
print("FIRST QUERY \n\n")
con = sqlite3.connect(database="rms.db")
cur = con.cursor()
cur.execute("select s.name,s.address,r.marks_ob from student s,result r where s.roll=r.roll and r.marks_ob between 35 and 50")
rows=cur.fetchall()
for r in rows:
    print(r)
print("SECOND QUERY \n\n")
# cur.execute("create view sharath as select s.name,s.dob, r.marks_ob*1.1 as new_marks from student s, result r where s.roll=r.roll and r.marks_ob between 25 and 35 and r.course='dbms'")
cur.execute("select * from sharath")
cur.execute("SELECT COUNT(*) AS student_count FROM sharath")
rows=cur.fetchall()
for r in rows:
    print(r)
