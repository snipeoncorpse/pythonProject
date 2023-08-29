from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ','Natürlich ist er das!')
    quit()

def motionMouse(event, btnNo=None):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))
    btnGatter.place(x=random.randint(0, 300), y=random.randint(0, 300))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'aquamarine'

label=Label(root,text='Ist Herr Lehnen Toll?',font='Arial 20 bold',bg='white').pack()
btnYes = Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)

btnNo = Button(root, text='Yes', font= 'Arial 20 bold', command=no).place(x=350, y=120)
btnGatter = Button(root, text='Gatter', font= 'Arial 20 bold', command=no).place(x=350, y=50)
btnSageratter = Button(root, text='Sageratter', font= 'Arial 20 bold', command=no).place(x=350, y=190)

root.mainloop()