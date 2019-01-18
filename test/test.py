# from tkinter import *

# window = Tk()
# window.geometry("600x400")
# window.title("Test :)")


# window.mainloop()
from tkinter import *

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Würfel')
tkFenster.geometry('1024x1024')

# Canvas für den Hintergrund
imageHintergrund = PhotoImage(file='smb.png')
canvasHintergrund = Canvas(master=tkFenster)
canvasHintergrund.place(x=0, y=0, width=1024, height=1024)
canvasHintergrund.create_image(0, 0, image=imageHintergrund, anchor='nw')

# Aktivierung des Fensters
tkFenster.mainloop()