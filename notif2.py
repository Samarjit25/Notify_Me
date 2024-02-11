from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Notify Me')
t.geometry("500x300")
img =Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)

#fetch_details

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

img_label = Label(t, image=tkimage).grid()

#Label_Title
t_label = Label(t, text="Title",font=("poppins", 10))
t_label.place(x=12, y=70)

#Entry_Title
title = Entry(t, width="25", font=("poppins", 13))
title.place(x=123, y=70)

#Label_Msg
m_label = Label(t, text="Message",font=("poppins", 10))
m_label.place(x=12, y=120)

#Entry_Msg
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30,y=120)

#Label_Time
time_label = Label(t, text="Time",font=("poppins", 10))
time_label.place(x=12, y=175)

#Entry_Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123,y=175)

#Label_min
time_min_label = Label(t, text ="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

#Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg ="#ffffff", bg="#000000", width =20, relief="raised",command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()
