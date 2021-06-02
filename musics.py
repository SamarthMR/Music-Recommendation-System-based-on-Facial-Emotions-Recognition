import pygame
from tkinter import *
import pygame.mixer
import os
import ntpath

pygame.init()
pygame.mixer.init()
root = Tk()
root.geometry("1600x800+0+0")
root.configure(background="powder blue")
Tops = Frame(root, width=1350, height=50, bd=8, bg="powder blue")
Tops.pack(side=TOP)

lblinfo = Label(Tops, font=('arial', 40, 'bold'), text="Advanced Music Player ", bd=10, fg="green")
lblinfo.grid(row=0, column=0)
list = []
list5 = []
for rt, dirs, files in os.walk('C:/music'):
    for file in files:
        if file.endswith('.mp3'):
            list.append(os.path.join(rt, file))
        if file.endswith('.mpeg'):
            list.append(os.path.join(rt, file))
txtdisplay = Listbox(root, height=23, width=38, bd=16, font=('arial', 15, 'bold'), fg="green", bg="powder blue")
txtdisplay.place(relx=0.7, rely=0.5, anchor=CENTER)
i = 0
for name in list:
    list5.append(ntpath.basename(name))
    txtdisplay.insert(END, list5[i])
    i += 1
index = 0


def showinfo(param, param1):
    pass


def next():
    global index
    index += 1
    if index == len(list):
        btn5['state'] = 'disabled'
        pygame.mixer.music.stop()
        txtdisplay.itemconfig(index-1, {'fg': 'green'})
        index = 0
        showinfo("FYI", "your songs are over if u want listen once again press play button to continue?")
    else:
        txtdisplay.itemconfig(index-1, {'fg': 'green'})
        txtdisplay.itemconfig(index, {'fg': 'red'})
        pygame.mixer.music.load(list[index])
        pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def previous():
    global index
    index -= 1
    if index == -1:
        pygame.mixer.music.stop()
        txtdisplay.itemconfig(index+1, {'fg': 'green'})
        showinfo("FYI", "your previous songs are over if u want play from starting press play button continue?")
        index = 0
    else:
        txtdisplay.itemconfig(index, {'fg': 'red'})
        txtdisplay.itemconfig(index+1, {'fg': 'green'})
        pygame.mixer.music.load(list[index])
        pygame.mixer.music.play()


def play():
    global index
    btn5['state'] = 'normal'
    txtdisplay.itemconfig(index, {'fg': 'red'})
    pygame.mixer.music.load(list[index])
    pygame.mixer.music.play()


def __init__(self):
    def exit(self):
        exit = self.askyesno("music player", "are u sure u want to exit click(yes/no)?")
        if exit > 0:
            root.destroy()
        return


btn6 = Button(root, text="play", fg="powder blue", padx=10, pady=10, bd=4, width=10, bg="blue",
              font=('arial', 15, 'bold'), command=play)
btn6.place(relx=0.3, rely=0.3, anchor=CENTER)
btn5 = Button(root, text="next", fg="powder blue", bg="blue", padx=10, pady=10, bd=4, width=10, state="normal",
              font=('arial', 15, 'bold'), command=next)
btn5.place(relx=0.3, rely=0.4, anchor=CENTER)
btn1 = Button(root, text="stop", fg="powder blue", bg="red", padx=10, pady=10, bd=4, width=10,
              font=('arial', 15, 'bold'), command=stop)
btn1.place(relx=0.3, rely=0.5, anchor=CENTER)
btn2 = Button(root, text="pause", fg="powder blue", bg="yellow", padx=10, pady=10, bd=4, width=10,
              font=('arial', 15, 'bold'), command=pause)
btn2.place(relx=0.3, rely=0.6, anchor=CENTER)
btn3 = Button(root, text="unpause", fg="powder blue", bg="blue", padx=10, pady=10, bd=4, width=10,
              font=('arial', 15, 'bold'), command=unpause)
btn3.place(relx=0.3, rely=0.7, anchor=CENTER)
btn4 = Button(root, text="previous", fg="powder blue", bg="blue", padx=10, pady=10, bd=4, width=10,
              font=('arial', 15, 'bold'), command=previous)
btn4.place(relx=0.3, rely=0.8, anchor=CENTER)
btn7 = Button(root, text="Exit", fg="powder blue", bg="blue", padx=10, pady=10, bd=4, width=10,
              font=('arial', 15, 'bold'), command=exit)
btn7.place(relx=0.3, rely=0.8, anchor=CENTER)
root.mainloop()
