from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from view_result import ViewResult
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("student result management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #--icon--#
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_marks.png")


        #--icon--#

        title=Label(self.root,text="Student Result Management System",compound=LEFT,padx=10,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #---MENU----#
        M_Frame=LabelFrame(self.root,text="menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)
        btn_course=Button(M_Frame,text="course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.view_result).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)
        #------content_window---#
        self.bg_img=Image.open("images/image_marks.jpg")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_img=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #---update_details---#
        self.lbl_course=Label(self.root,text="Total courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total result\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        footer=Label(self.root,text="SRMS-Student Result Management System\n contact us for any technical issue 99801***02",font=("goudy old style",12),bg="#033054",fg="white").pack(side=BOTTOM,fill=X)
        #---MENU----#
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ViewResult(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()