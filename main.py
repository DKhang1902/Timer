from playsound import playsound
import tkinter as tk
import time

def count_down():
    t = int(input("How long?"))
    while t:
        mins = t//60
        secs = t % 60
        hours = 0
        if mins >= 60:
            mins = mins % 60
            hours = mins//60
        print("{:02d}:{:02d}:{:02d}".format(hours, mins, secs), end="\r")
        time.sleep(1)
        t -= 1
        if t == 0:
            break
    print("Blast off")
    playsound(r"C:\Users\duykh\Coding\Timer\samsung_alarm_remix.mp3")

def click():
    pass

root = tk.Tk()
root.title("Timer")
tk.Button(root, text="Setting", width=6, command=click).grid(row=0,column=0,sticky="W")
count_down()


tk.mainloop()
