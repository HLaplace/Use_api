import feedparser
from tkinter import *

entry = feedparser.parse("https://www.lemonde.fr/rss/une.xml")

class interface:

    def __init__(self):

        self.root = Tk()
        self.color = "#A2AFAD"
        self.root.title("Journal")
        self.root.config(background=self.color)
        self.root.geometry("960x720")
        self.root.minsize(480, 360)

        self.inside_wdw()

    def inside_wdw(self):

        # créer frame
        self.frame = Frame(self.root, bg=self.color)
        self.frame.pack(expand=YES)

        # consigne
        self.label_title = Label(self.frame, text=entry['entries'][0]['title'], font=("Arial", 30),
                               fg="black", bg=self.color)
        self.label_title.pack(expand=YES)

        # Couleur
        self.label_description = Label(self.frame, text=entry['entries'][0]['description'], font=("Arial", 20), bg=self.color)
        self.label_description.pack(expand=YES)

        self.root.mainloop()

main = interface()
