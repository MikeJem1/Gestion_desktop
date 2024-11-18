import tkinter as tk
from tkinter import ttk, messagebox
# importation des autres module pour finir le menu principale

def mainMenu():
    global root

    root =tk.Tk()
    root.title("MENU PRINCIPAL")

    #deconnexion
    btn_deconnecter=tk.Button(root, text="Deconnecter",)
    btn_deconnecter.pack(pady=10)

    #navigation
    frame_navigation=tk.Frame(root)
    frame_navigation.pack(pady=10)

    btn_bon_livraison= tk.Button(frame_navigation, text="bon de livraison")
    btn_bon_livraison.grid(row=0, column=0, padx=5)

    btn_produit = tk.Button(frame_navigation, text="Gestion des produits ")
    btn_produit.grid(row=0, column=2, padx=5)

    
    btn_commande = tk.Button(frame_navigation, text="Gestion des commandes")
    btn_commande.grid(row=0, column=3, padx=5)

    
    btn_client = tk.Button(frame_navigation, text="Gestion des Clients")
    btn_client.grid(row=0, column=4, padx=5)

    btn_compte=tk.Button(frame_navigation, text="compte des Clients")
    btn_compte.grid(row=1, column=0,padx=5)

    btn_ligne=tk.Button(frame_navigation, text="Gestion de Ligne de commande")
    btn_ligne.grid(row=1, column=0,padx=5)


    root.mainloop()



if __name__=="__main__":
    mainMenu()