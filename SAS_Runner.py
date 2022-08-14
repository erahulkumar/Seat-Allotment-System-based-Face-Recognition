import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time

# Window is our Main frame of system
window = tk.Tk()
window.title("SAS-Face Recognition Based Seat Allotment System")
window.geometry('1280x720')
frame = Frame(window, width=1280, height=720)
frame.pack()
frame.place(anchor='center', rely=0.5, relx=0.5)
window.configure(background='snow')
imgs = ImageTk.PhotoImage(Image.open("Image/bg.jpg"))
label1 = Label(frame, image=imgs)
label1.pack()


# GUI for manually fill attendance

def manually_fill():
    sb = tk.Tk()
    sb.iconbitmap('SAS.ico')
    sb.title("Enter subject name...")
    sb.geometry('580x320')
    sb.configure(background='snow')

    def err_screen_for_subject():

        def ec_delete():
            ec.destroy()

        ec = tk.Tk()
        ec.geometry('300x100')
        ec.iconbitmap('SAS.ico')
        ec.title('Warning!!')
        ec.configure(background='snow')
        Label(ec, text='Please enter your subject name!!!', fg='red', bg='white', font=('times', 16, ' bold ')).pack()
        Button(ec, text='OK', command=ec_delete, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
               font=('times', 15, ' bold ')).place(x=90, y=50)

    def fill_attendance():
        ts = time.time()
        Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        # Creating csv of attendance

        # Create table for Attendance
        date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        global subb
        subb = SUB_ENTRY.get()
        DB_table_name = str(subb + "_" + Date + "_Time_" + Hour + "_" + Minute + "_" + Second)

        import pymysql.connections
        global cursor
        # Connect to the database
        try:

            connection = pymysql.connect(host='localhost', user='root', password='', db='manually_fill_attendance')
            cursor = connection.cursor()
        except Exception as e:
            print(e)

        sql = "CREATE TABLE " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT, 
                         ROLL varchar(100) NOT NULL,
                         NAME VARCHAR(50) NOT NULL,
                         SEAT VARCHAR(50) NOT NULL,
                         ADDRESS VARCHAR(100) NOT NULL,
                         MOBILE VARCHAR(10) NOT NULL,
                         EXAM VARCHAR(50) NOT NULL,
                         EADDRESS VARCHAR(100) NOT NULL,
                         DATE VARCHAR(20) NOT NULL,
                         TIME VARCHAR(20) NOT NULL,
                             PRIMARY KEY (ID)
                             );
                        """

        try:
            cursor.execute(sql)
            # for create a table
        except Exception as ex:
            print(ex)  #

        if subb == '':
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Tk()
            MFW.iconbitmap('SAS.ico')
            MFW.title("Manually attendance of " + str(subb))
            MFW.geometry('880x470')
            MFW.configure(background='snow')

            def del_errsc2():
                errsc2.destroy()

            def err_screen1():
                global errsc2
                errsc2 = tk.Tk()
                errsc2.geometry('330x100')
                errsc2.iconbitmap('SAS.ico')
                errsc2.title('Warning!!')
                errsc2.configure(background='snow')
                Label(errsc2, text='Please enter Student & ROLLNO!!!', fg='red', bg='white',
                      font=('times', 16, ' bold ')).pack()
                Button(errsc2, text='OK', command=del_errsc2, fg="black", bg="lawn green", width=9, height=1,
                       activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)

            def testVal(inStr, acttyp):
                if acttyp == '1':  # insert
                    if not inStr.isdigit():
                        return False
                return True

            def remove_all():
                ENR_ENTRY.delete(first=0, last=22)
                STUDENT_ENTRY.delete(first=0, last=22)
                SEAT_ENTRY.delete(first=0, last=22)
                ADDRESS_ENTRY.delete(first=0, last=22)
                MOBILE_ENTRY.delete(first=0, last=22)
                EXAM_ENTRY.delete(first=0, last=22)
                EADDRESS_ENTRY.delete(first=0, last=22)

            def remove_enr():
                ENR_ENTRY.delete(first=0, last=22)

            def remove_student():
                STUDENT_ENTRY.delete(first=0, last=22)

            ENR = tk.Label(MFW, text="Roll Number", width=20, height=1, fg="white", bg="blue2",
                           font=('times', 12, ' bold '))
            ENR.place(x=50, y=50)

            STU_NAME = tk.Label(MFW, text="Student name", width=20, height=1, fg="white", bg="blue2",
                                font=('times', 12, ' bold '))
            STU_NAME.place(x=50, y=80)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(MFW, width=20, validate='key', bg="yellow", fg="red", font=('times', 12, ' bold '))
            ENR_ENTRY['validatecommand'] = (ENR_ENTRY.register(testVal), '%P', '%d')
            ENR_ENTRY.place(x=260, y=50)

            STUDENT_ENTRY = tk.Entry(MFW, width=20, bg="yellow", fg="red", font=('times', 12, ' bold '))
            STUDENT_ENTRY.place(x=260, y=80)

            SEATs = tk.Label(MFW, text='Seat Number ', width=20, bg="blue2", fg="white", font=('times', 12, ' bold '))
            SEATs.place(x=50, y=110)

            SEAT_ENTRY = tk.Entry(MFW, width=20, bg="yellow", fg="red", font=('times', 12, ' bold '))
            SEAT_ENTRY.place(x=260, y=110)

            ADDRESSs = tk.Label(MFW, text='Address ', width=20, bg="blue2", fg="white", font=('times', 12, ' bold '))
            ADDRESSs.place(x=50, y=140)

            ADDRESS_ENTRY = tk.Entry(MFW, width=20, bg="yellow", fg="red", font=('times', 12, ' bold '))
            ADDRESS_ENTRY.place(x=260, y=140)

            MOBILEs = tk.Label(MFW, text='Mobile Number ', width=20, bg="blue2", fg="white",
                               font=('times', 12, ' bold '))
            MOBILEs.place(x=50, y=170)

            MOBILE_ENTRY = tk.Entry(MFW, width=20, validate='key', bg="yellow", fg="red", font=('times', 12, ' bold '))
            MOBILE_ENTRY['validatecommand'] = (MOBILE_ENTRY.register(testVal), '%P', '%d')
            MOBILE_ENTRY.place(x=260, y=170)

            EXAMs = tk.Label(MFW, text='Exam center name ', width=20, bg="blue2", fg="white",
                             font=('times', 12, ' bold '))
            EXAMs.place(x=50, y=200)

            EXAM_ENTRY = tk.Entry(MFW, width=20, bg="yellow", fg="red", font=('times', 12, ' bold '))
            EXAM_ENTRY.place(x=260, y=200)

            EADDRESSs = tk.Label(MFW, text='Exam address', width=20, bg="blue2", fg="white",
                                 font=('times', 12, ' bold '))
            EADDRESSs.place(x=50, y=230)

            EADDRESS_ENTRY = tk.Entry(MFW, width=20, bg="yellow", fg="red", font=('times', 12, ' bold '))
            EADDRESS_ENTRY.place(x=260, y=230)

            # get important variable
            def enter_data_DB():
                ROLL = ENR_ENTRY.get()
                STUDENT = STUDENT_ENTRY.get()
                SEAT = SEAT_ENTRY.get()
                ADDRESS = ADDRESS_ENTRY.get()
                MOBILE = MOBILE_ENTRY.get()
                EXAM = EXAM_ENTRY.get()
                EADDRESS = EADDRESS_ENTRY.get()
                if ROLL == '':
                    err_screen1()
                elif STUDENT == '':
                    err_screen1()
                else:
                    time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    Hour, Minute, Second = time.split(":")
                    Insert_data = "INSERT INTO " + DB_table_name + "(ID,ROLL,NAME,SEAT,ADDRESS,MOBILE,EXAM,EADDRESS,DATE,TIME) VALUES (0, %s, %s, %s,%s, %s, %s, %s, %s, %s) "
                    VALUES = (
                        str(ROLL), str(STUDENT), str(SEAT), str(ADDRESS), str(MOBILE), str(EXAM), str(EADDRESS),
                        str(Date),
                        str(time))
                    try:
                        cursor.execute(Insert_data, VALUES)
                        MSG = tk.Label(MFW, text='Manually Seat Allot Successfully', width=20, bg="blue2", fg="white",
                                       font=('times', 12, ' bold '))
                        MSG.place(x=180, y=380)
                    except Exception as e:
                        print(e)

            def create_csv():
                import csv
                cursor.execute("select * from " + DB_table_name + ";")
                csv_name = 'C:/Users/errah/PycharmProjects/Seat Allotment system/Attendance/Manually Attendance/' + DB_table_name + '.csv'
                with open(csv_name, "w") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                    csv_writer.writerows(cursor)
                    alr = "CSV created Successfully"
                    Notifi.configure(text=alr, bg="Green", fg="white", width=33, font=('times', 19, 'bold'))
                    Notifi.place(x=180, y=380)
                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Attendance of " + subb)
                root.configure(background='snow')
                with open(csv_name, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(root, width=13, height=1, fg="black", font=('times', 13, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()

            Notifi = tk.Label(MFW, text="CSV created Successfully", bg="Green", fg="white", width=33,
                              height=2, font=('times', 19, 'bold'))

            clear_all = tk.Button(MFW, text="All Clear", command=remove_all, fg="black", bg="deep pink", width=20,
                                  height=1, activebackground="Red", font=('times', 15, ' bold '))
            clear_all.place(x=50, y=300)

            DATA_SUB = tk.Button(MFW, text="Enter Data", command=enter_data_DB, fg="black", bg="lime green", width=20,
                                 height=1, activebackground="Red", font=('times', 15, ' bold '))
            DATA_SUB.place(x=310, y=300)

            MAKE_CSV = tk.Button(MFW, text="Convert to CSV", command=create_csv, fg="black", bg="red", width=20,
                                 height=1,
                                 activebackground="Red", font=('times', 15, ' bold '))
            MAKE_CSV.place(x=570, y=300)

            def attf():
                import subprocess
                subprocess.Popen(
                    r'explorer /select,"C:\Users\errah\PycharmProjects\Seat Allotment system\Attendance\Manually '
                    r'Attendance\"')

            attf = tk.Button(MFW, text="Check Sheets", command=attf, fg="black", bg="lawn green", width=12, height=1,
                             activebackground="Red", font=('times', 14, ' bold '))
            attf.place(x=730, y=410)

            MFW.mainloop()

    SUB = tk.Label(sb, text="Enter Subject", width=15, height=2, fg="white", bg="blue2", font=('times', 15, ' bold '))
    SUB.place(x=30, y=100)

    global SUB_ENTRY

    SUB_ENTRY = tk.Entry(sb, width=20, bg="yellow", fg="red", font=('times', 23, ' bold '))
    SUB_ENTRY.place(x=250, y=105)

    fill_manual_attendance = tk.Button(sb, text="Fill Attendance", command=fill_attendance, fg="white", bg="deep pink",
                                       width=20, height=2,
                                       activebackground="Red", font=('times', 15, ' bold '))
    fill_manual_attendance.place(x=250, y=160)
    sb.mainloop()


# For clear textbox
def clear():
    txt.delete(first=0, last=22)


def clear1():
    txt2.delete(first=0, last=22)


def clear3():
    txt3.delete(first=0, last=22)


def clear4():
    txt4.delete(first=0, last=22)


def clear5():
    txt5.delete(first=0, last=22)


def clear6():
    txt6.delete(first=0, last=22)


def del_sc1():
    sc1.destroy()


def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry('300x100')
    sc1.iconbitmap('SAS.ico')
    sc1.title('Warning!!')
    sc1.configure(background='snow')
    Label(sc1, text='Please fill all input box required!!!', fg='red', bg='white', font=('times', 16, ' bold ')).pack()
    Button(sc1, text='OK', command=del_sc1, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
           font=('times', 15, ' bold ')).place(x=90, y=50)


# Error screen2
def del_sc2():
    sc2.destroy()


def err_screen1():
    global sc2
    sc2 = tk.Tk()
    sc2.geometry('300x100')
    sc2.iconbitmap('AMS.ico')
    sc2.title('Warning!!')
    sc2.configure(background='snow')
    Label(sc2, text='Please enter your subject name!!!', fg='red', bg='white', font=('times', 16, ' bold ')).pack()
    Button(sc2, text='OK', command=del_sc2, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
           font=('times', 15, ' bold ')).place(x=90, y=50)


# For take images for datasets
def take_img():
    l1 = txt.get()
    l2 = txt2.get()
    l3 = txt3.get()
    l4 = txt4.get()
    l5 = txt5.get()
    l6 = txt6.get()
    l7 = txt7.get()
    if l1 == '':
        err_screen()
    elif l2 == '':
        err_screen()
    elif l3 == '':
        err_screen()
    elif l4 == '':
        err_screen()
    elif l5 == '':
        err_screen()
    elif l6 == '':
        err_screen()
    elif l7 == '':
        err_screen()
    else:
        try:
            cam = cv2.VideoCapture(0)
            detectors = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            Roll = txt.get()
            Name = txt2.get()
            Seat = txt3.get()
            Address = txt4.get()
            Mobile = txt5.get()
            Exam = txt6.get()
            Eaddress = txt7.get()
            sampleNum = 0
            while True:
                ret, img = cam.read(0)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detectors.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder
                    cv2.imwrite("TrainingImage/ " + Name + "." + Roll + '.' + Seat + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    cv2.imshow('Camera Capturing ....', img)
                # wait for 100 milliseconds
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # break if the sample number is more than 100
                elif sampleNum > 50:
                    break
            cam.release()
            cv2.destroyAllWindows()
            ts = time.time()
            Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            row = [Roll, Name, Seat, Address, Mobile, Exam, Eaddress, Date, Time]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for Roll No. : " + Roll + " Name : " + Name + " Seat :" + Seat
            Notification.configure(text=res, bg="SpringGreen3", height=1, width=40, font=('times', 15, 'bold'))
            Notification.place(x=350, y=400)
        except FileExistsError as F:
            f = 'Student Data already exists'
            Notification.configure(text=f, bg="Red", width=21)
            Notification.place(x=450, y=600)


# for choose subject and fill attendance
def subjectchoose():
    def Fillattendances():
        sub = tx.get()
        now = time.time()
        # For calculate seconds of video
        future = now + 20
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                try:
                    recognizer.read("TrainingImageLabel\Trainner.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=20, y=250)

                harcascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                df = pd.read_csv("StudentDetails\StudentDetails.csv")
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ['Roll', 'Name', 'Seat', 'Address', 'Mobile', 'Exam', 'Eaddress', 'Date', 'Time']
                attendance = pd.DataFrame(columns=col_names)
                global Subject
                global aa
                global Id
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        # global Id
                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if conf < 50:
                            print(conf)
                            global Subject
                            # global aa
                            global date
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            aa = df.loc[df['Roll'] == Id]['Name'].values
                            global tt
                            tt = str(Id) + "-" + aa
                            En = '15624031' + str(Id)
                            attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)

                        else:
                            Id = 'Unknown'
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(['Roll'], keep='first')
                    cv2.imshow('Filling attendance..', im)
                    key = cv2.waitKey(30) & 0xff
                    if key == 27:
                        break

                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Hour, Minute, Second = timeStamp.split(":")
                fileName = "Attendance/" + Subject + "_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
                attendance = attendance.drop_duplicates(['Roll'], keep='first')
                print(attendance)
                attendance.to_csv(fileName, index=False)

                # Create table for Attendance
                date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
                DB_Table_name = str(Subject + "_" + date_for_DB + "_Time_" + Hour + "_" + Minute + "_" + Second)
                import pymysql.connections

                # Connect to the database
                try:
                    global cursor
                    connection = pymysql.connect(host='localhost', user='root', password='', db='Face_reco_fill')
                    cursor = connection.cursor()
                except Exception as e:
                    print(e)

                sql = "CREATE TABLE " + DB_Table_name + """
                (ID INT NOT NULL AUTO_INCREMENT,
                 ROLL varchar(100) NOT NULL,
                 NAME VARCHAR(50) NOT NULL,
                 SEAT VARCHAR(50) NOT NULL,
                 ADDRESS VARCHAR(100) NOT NULL,
                 MOBILE VARCHAR(10) NOT NULL,
                 EXAM VARCHAR(50) NOT NULL,
                 EADDRESS VARCHAR(100) NOT NULL,
                 DATE VARCHAR(20) NOT NULL,
                 TIME VARCHAR(20) NOT NULL,
                     PRIMARY KEY (ID)
                     );
                """
                # Now enter attendance in Database
                insert_data = "INSERT INTO " + DB_Table_name + "(ID,ROLl,NAME,SEAT,ADDRESS,MOBILE,EXAM,EADDRESS,DATE,TIME) VALUES (0, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
                VALUES = (str(Id), str(aa), str(date), str(timeStamp))
                try:
                    cursor.execute(sql)
                    # for create a table
                    cursor.execute(insert_data, VALUES)
                    # For insert data into table
                except Exception as ex:
                    print(ex)

                M = 'Attendance filled Successfully'
                Notifica.configure(text=M, bg="Green", fg="white", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=20, y=250)

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Attendance of " + Subject)
                root.configure(background='snow')
                cs = 'C:/Users/errah/PycharmProjects/Seat Allotment system/' + fileName
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
                print(attendance)

    # windo is frame for subject chooser
    windo = tk.Tk()
    windo.iconbitmap('SAS.ico')
    windo.title("Enter subject name...")
    windo.geometry('580x320')
    windo.configure(background='snow')
    Notifica = tk.Label(windo, text="Attendance filled Successfully", bg="Green", fg="white", width=33,
                        height=2, font=('times', 15, 'bold'))

    def Attf():
        import subprocess
        subprocess.Popen(
            r'explorer /select,"C:\Users\errah\PycharmProjects\Seat Allotment system\Attendance"')

    Attf = tk.Button(windo, text="Check Sheets", command=Attf, fg="black", bg="lawn green", width=12, height=1,
                     activebackground="Red", font=('times', 14, ' bold '))
    Attf.place(x=430, y=255)

    sub = tk.Label(windo, text="Enter Subject", width=15, height=2, fg="white", bg="blue2",
                   font=('times', 15, ' bold '))
    sub.place(x=30, y=100)

    tx = tk.Entry(windo, width=20, bg="yellow", fg="red", font=('times', 23, ' bold '))
    tx.place(x=250, y=105)

    fill_a = tk.Button(windo, text="Fill Attendance", fg="white", command=Fillattendances, bg="deep pink", width=20,
                       height=2,
                       activebackground="Red", font=('times', 15, ' bold '))
    fill_a.place(x=250, y=160)
    windo.mainloop()


def admin_panel():
    win = tk.Tk()
    win.iconbitmap('SAS.ico')
    win.title("LogIn")
    win.geometry('880x420')
    win.configure(background='snow')

    def log_in():
        username = un_entr.get()
        password = pw_entr.get()

        if username == 'SAS':
            if password == 'SAS@123':
                win.destroy()
                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Student Details")
                root.configure(background='snow')

                cs = 'C:/Users/errah/PycharmProjects/Seat Allotment system/StudentDetails/StudentDetails.csv'
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
            else:
                valid = 'Incorrect ID or Password'
                Nt.configure(text=valid, bg="red", fg="black", width=38, font=('times', 19, 'bold'))
                Nt.place(x=120, y=350)

        else:
            valid = 'Incorrect ID or Password'
            Nt.configure(text=valid, bg="red", fg="black", width=38, font=('times', 19, 'bold'))
            Nt.place(x=120, y=350)

    Nt = tk.Label(win, text="Attendance filled Successfully", bg="Green", fg="white", width=40,
                  height=2, font=('times', 19, 'bold'))
    # Nt.place(x=10, y=35)

    un = tk.Label(win, text="Enter username", width=15, height=2, fg="white", bg="blue2",
                  font=('times', 15, ' bold '))
    un.place(x=30, y=50)

    pw = tk.Label(win, text="Enter password", width=15, height=2, fg="white", bg="blue2",
                  font=('times', 15, ' bold '))
    pw.place(x=30, y=150)

    def c00():
        un_entr.delete(first=0, last=22)

    un_entr = tk.Entry(win, width=20, bg="yellow", fg="red", font=('times', 23, ' bold '))
    un_entr.place(x=290, y=55)

    def c11():
        pw_entr.delete(first=0, last=22)

    pw_entr = tk.Entry(win, width=20, show="*", bg="yellow", fg="red", font=('times', 23, ' bold '))
    pw_entr.place(x=290, y=155)

    c0 = tk.Button(win, text="Clear", command=c00, fg="black", bg="deep pink", width=10, height=1,
                   activebackground="Red", font=('times', 15, ' bold '))
    c0.place(x=690, y=55)

    c1 = tk.Button(win, text="Clear", command=c11, fg="black", bg="deep pink", width=10, height=1,
                   activebackground="Red", font=('times', 15, ' bold '))
    c1.place(x=690, y=155)

    Login = tk.Button(win, text="LogIn", fg="black", bg="lime green", width=20,
                      height=2,
                      activebackground="Red", command=log_in, font=('times', 15, ' bold '))
    Login.place(x=290, y=250)
    win.mainloop()


# For train the model
def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    global faces, Id
    try:
        # global faces, Id
        faces, Id = getImagesAndLabels("TrainingImage")
    except Exception as e:
        l = 'please make "TrainingImage" folder & put Images'
        Notification.configure(text=l, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("TrainingImageLabel\Trainner.yml")
    except Exception as e:
        q = 'Please make "TrainingImageLabel" folder'
        Notification.configure(text=q, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    res = "Model Trained"  # +",".join(str(f) for f in Id)
    Notification.configure(text=res, bg="SpringGreen3", width=40, font=('times', 15, 'bold'))
    Notification.place(x=250, y=600)


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empty face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the ID from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = detector.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as ID of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.iconbitmap('SAS.ico')


def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

message = tk.Label(window, text="Face-Recognition-Based-Seat-Allotment-System", bg="cyan", fg="black", width=80,
                   height=2, font=('times', 25, 'italic bold '))
message.place(x=0, y=0)

Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                        height=3, font=('times', 17, 'bold'))

lbl = tk.Label(window, text="1.Enter Roll No.", width=20, height=1, fg="black", bg="deep pink",
               font=('times', 15, ' bold '))
lbl.place(x=40, y=100)


def testVal(inStr, acttyp):
    if acttyp == '1':  # insert
        if not inStr.isdigit():
            return False
    return True


txt = tk.Entry(window, validate="key", width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt['validatecommand'] = (txt.register(testVal), '%P', '%d')
txt.place(x=300, y=100)

lbl2 = tk.Label(window, text="2.Enter Name", width=20, fg="black", bg="deep pink", height=1,
                font=('times', 15, ' bold '))
lbl2.place(x=40, y=160)

txt2 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt2.place(x=300, y=160)

clearButton = tk.Button(window, text="Clear", command=clear, fg="white", bg="black", width=10, height=1,
                        activebackground="Red", font=('times', 10, ' bold '))
clearButton.place(x=520, y=100)

clearButton1 = tk.Button(window, text="Clear", command=clear1, fg="white", bg="black", width=10, height=1,
                         activebackground="Red", font=('times', 10, ' bold '))
clearButton1.place(x=520, y=160)

lbl3 = tk.Label(window, text="3.Seat Number", width=20, height=1, fg="black", bg="deep pink",
                font=('times', 15, ' bold '))
lbl3.place(x=40, y=220)

txt3 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt3.place(x=300, y=220)

clearButton3 = tk.Button(window, text="Clear", command=clear3, fg="white", bg="black", width=10, height=1,
                         activebackground="Red", font=('times', 10, ' bold '))
clearButton3.place(x=520, y=220)

lbl4 = tk.Label(window, text="4.Address", width=20, height=1, fg="black", bg="deep pink",
                font=('times', 15, ' bold '))
lbl4.place(x=40, y=280)

txt4 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt4.place(x=300, y=280)

clearButton4 = tk.Button(window, text="Clear", command=clear4, fg="white", bg="black", width=10, height=1,
                         activebackground="Red", font=('times', 10, ' bold '))
clearButton4.place(x=520, y=280)

lbl5 = tk.Label(window, text="5.Mobile No.", width=20, height=1, fg="black", bg="deep pink",
                font=('times', 15, ' bold '))
lbl5.place(x=40, y=340)

txt5 = tk.Entry(window, validate="key", width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt5['validatecommand'] = (txt5.register(testVal), '%P', '%d')
txt5.place(x=300, y=340)

clearButton5 = tk.Button(window, text="Clear", command=clear5, fg="white", bg="black", width=10, height=1,
                         activebackground="Red", font=('times', 10, ' bold '))
clearButton5.place(x=520, y=340)

lbl6 = tk.Label(window, text="6.Exam Center Name", width=20, height=1, fg="black", bg="deep pink",
                font=('times', 15, ' bold '))
lbl6.place(x=620, y=100)

txt6 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt6.place(x=880, y=100)

clearButton6 = tk.Button(window, text="Clear", command=clear6, fg="white", bg="black", width=10, height=1,
                         activebackground="Red", font=('times', 10, ' bold '))
clearButton6.place(x=1100, y=100)

lbl7 = tk.Label(window, text="7.Address Exam Center", width=20, height=1, fg="black", bg="deep pink",
                font=('times', 15, ' bold '))
lbl7.place(x=620, y=160)

txt7 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt7.place(x=880, y=160)

clearButton7 = tk.Button(window, text="Clear", command=clear6, fg="white", bg="black", width=10, height=1,
                         activebackground="Red", font=('times', 10, ' bold '))
clearButton7.place(x=1100, y=160)

AP = tk.Button(window, text="Admin Panel", command=admin_panel, fg="black", bg="cyan", width=19, height=1,
               activebackground="Red", font=('times', 15, ' bold '))
AP.place(x=990, y=600)

takeImg = tk.Button(window, text="1.Take Images", command=take_img, fg="white", bg="blue2", width=20, height=2,
                    activebackground="Red", font=('times', 15, ' bold '))
takeImg.place(x=90, y=500)

trainImg = tk.Button(window, text="2.Train Images", fg="black", command=trainimg, bg="lawn green", width=20, height=2,
                     activebackground="Red", font=('times', 15, ' bold '))
trainImg.place(x=390, y=500)

FA = tk.Button(window, text="3.Automatic Attendance", fg="white", command=subjectchoose, bg="blue2", width=20, height=2,
               activebackground="Red", font=('times', 15, ' bold '))
FA.place(x=690, y=500)

quitWindow = tk.Button(window, text="4.Manually Fill Attendance", command=manually_fill, fg="black", bg="lawn green",
                       width=20, height=2, activebackground="Red", font=('times', 15, ' bold '))
quitWindow.place(x=990, y=500)

window.mainloop()
