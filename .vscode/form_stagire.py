from sys import path

#from tp_TSDI_PY.users.stagire import Stagire
# path.append("/home/karim/TSDI")
import tkinter as tk
from tkinter import messagebox as msg
from etablissement import Etablissement



class FormStagire:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("stagire")

        self.root.mainloop()

