from etablissement import Etablissement
import tkinter as tk
from stagire import Stagire
from tkinter import messagebox as msg

class GestionStagire:
    def __init__(self):
        self.e=Etablissement("espigic", "lot nassr", "999", "kkjkj")
        self.e.charger()
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title(" Gestion de Stagire")
        self.lblNumIus = tk.Label(self.root, text="numIus")
        self.lblNumIus.grid(row=0, column=0, pady=10, padx=60)
        self.entryNumIus = tk.Entry(self.root)
        self.entryNumIus.grid(row=0, column=1)
        self.lblLogin = tk.Label(self.root, text="login")
        self.lblLogin.grid(row=1, column=0, pady=10, padx=60)
        self.entryLogin = tk.Entry(self.root)
        self.entryLogin.grid(row=1, column=1)
        self.lblPwd = tk.Label(self.root, text="Password")
        self.lblPwd.grid(row=2, column=0, pady=10, padx=60)
        self.entryPWD = tk.Entry(self.root)
        self.entryPWD.grid(row=2, column=1)

        self.btnAdd = tk.Button(self.root, text="add",command=self.add)
        self.btnAdd.grid(row=3, column=0)
        self.btnShow = tk.Button(self.root, text="show")
        self.btnShow.grid(row=3, column=1, sticky="w")
        self.btnSave = tk.Button(self.root, text="save")
        self.btnSave.grid(row=3, column=1, sticky="e")
        self.btnExit = tk.Button(self.root, text="exit")
        self.btnExit.grid(row=3, column=5, padx=40)

        self.root.mainloop()

    def save(self):
        self.e.save()

    def add(self):
        try :           
            self.e.ajouter(Stagire(self.entryNumIus.get(), self.entryLogin.get(), self.entryPWD.get()))
        except Exception as ex:
            msg.showwarning("error", ex)
            
        
