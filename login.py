import connexion_dataa
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3



#la verification de la connection 
def verification_connection(username, password):
    conn= sqlite3.connect('') # le nom du base de donnees dans votre rep
    cur= conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?', (username, password)")
    user=cur.fetchone()
    conn.close()

    if user:
        return True
    return False

def connexion():
    username = entry_username.get()
    password= entry_password.get()
    
    if verification_connection(username, password):
        messagebox.showinfo("info", "connexion reussie")
        root_connexion.destroy()
        #nouvelle page a ouvrir
    else:
        messagebox.showerror("erreur", "nom d'utilisateur ou mot de passe est incorrect")

def ecran_connexion():
    global root_connexion, entry_username, entry_password

    root_connexion = tk.Tk()
    root_connexion.title("Connexion à la base de données")

    tk.Label(root_connexion, text="Nom d'utilisateur").grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(root_connexion)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root_connexion, text="Mot de passe").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(root_connexion, show='*')
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    btn_connecter = tk.Button(root_connexion, text="Connecter", command=connexion)
    btn_connecter.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root_connexion.mainloop()



if __name__ == "__main__":
    ecran_connexion()
