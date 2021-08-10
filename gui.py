import tkinter as tk
from tkinter import font 
from tkinter import messagebox
from PIL import Image,ImageTk
import serial 
import time
import serial.tools.list_ports 


mainForm = tk.Tk()
mainForm.geometry('400x300+100+200')
mainForm.config(bg='black')
mainForm.title(' İnformation Panel ')
mainForm.resizable(False,False)

username = tk.StringVar(mainForm)
password = tk.StringVar(mainForm)

grayImage = ImageTk.PhotoImage(Image.open('***')) # Button file path's
redImage = ImageTk.PhotoImage(Image.open('***'))
yellowImage = ImageTk.PhotoImage(Image.open('***'))
greenImage = ImageTk.PhotoImage(Image.open('***'))
blueImage = ImageTk.PhotoImage(Image.open('***'))

nameLabel = tk.Label(mainForm,text=' Username : ',font='arial 20 bold',bg='black',fg='white').place(x=20,y=49)
passwordLabel = tk.Label(mainForm,text=' Password : ',font='arial 20 bold',bg='black',fg='white').place(x=20,y=149)

nameEntry = tk.Entry(mainForm,textvariable=username).place(x=200,y=60)
passwordEntry = tk.Entry(mainForm,show='*',textvariable=password).place(x=200,y=160)

def enter():
    if username.get()=='mertcan' and password.get()=='nane':
        okMessage=messagebox.showinfo('',' Successful !')

        data = str('0')
        numPort = str(' ')

        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            if "Port" in p.description:
                numPort = p.device
                
             
        communication = serial.Serial(port=numPort, baudrate=9600)

        if okMessage=='ok':
            sideForm = tk.Toplevel()
            mainForm.state('iconic')
            sideForm.geometry('1920x1080')
            sideForm.state('zoomed')
            sideForm.title(' Control Panel ')
            sideForm.config(bg='black')
            sideForm.resizable(False,False)


            def sendData(x):
                communication.write(bytes(x, 'utf-8'))
                time.sleep(0.05)

            def redOn():
                data='1'
                sendData(data)

            def redOff():
                data='2'
                sendData(data)

            def yellowOn():
                data='3'
                sendData(data)

            def yellowOff():
                data='4'
                sendData(data)

            def greenOn():
                data='5'
                sendData(data)

            def greenOff():
                data='6'
                sendData(data)

            def blueOn():
                data='7'
                sendData(data)

            def blueOff():
                data='8'
                sendData(data)
                   
            sendData('0')

            redOnButton = tk.Button(sideForm,activebackground='black',command=redOn,bg='black',image=redImage).place(x=1180,y=100)
            redOffButton = tk.Button(sideForm,activebackground='black',command=redOff,bg='black',image=grayImage).place(x=1180,y=500)

            yellowOnButton = tk.Button(sideForm,activebackground='black',command=yellowOn,bg='black',image=yellowImage).place(x=810,y=100)
            yellowOffButton = tk.Button(sideForm,activebackground='black',command=yellowOff,bg='black',image=grayImage).place(x=810,y=500)

            greenOnButton = tk.Button(sideForm,activebackground='black',command=greenOn,bg='black',image=greenImage).place(x=440,y=100)
            greenOffButton = tk.Button(sideForm,activebackground='black',command=greenOff,bg='black',image=grayImage).place(x=440,y=500)

            blueOnButton = tk.Button(sideForm,activebackground='black',command=blueOn,bg='black',image=blueImage).place(x=70,y=100)
            blueOffButton = tk.Button(sideForm,activebackground='black',command=blueOff,bg='black',image=grayImage).place(x=70,y=500)
    else:
            errorMessage=messagebox.showerror('',' Username or password is incorrect !')


def exit():
    mainForm.destroy()

enterButton = tk.Button(mainForm,text=' Enter ',activebackground='yellow',command=enter,font='arial  15 bold').place(x=80,y=230)
exitButton = tk.Button(mainForm,text=' Exit ',activebackground='yellow',command=exit,font='arial  15 bold').place(x=250,y=230)

mainForm.mainloop()

