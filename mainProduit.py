import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime




def menu_produit():
    global entry_numero_produit, entry_numero_famille, entry_date_rentrer, entry_designation, entry_quantite, entry_refference, entry_prix ,tree, root

    root = tk.Tk()
    root.title("Interface d'enregistrement des produit ")  

    # Ajout de commande
    frame_ajouter = tk.Frame(root)
    frame_ajouter.pack(pady=10)

    tk.Label(frame_ajouter, text="Numéro de produit:").grid(row=0, column=0)
    entry_numero_produit = tk.Entry(frame_ajouter)
    entry_numero_produit.grid(row=0, column=1)

    tk.Label(frame_ajouter, text="Numero famille:").grid(row=1, column=0)
    entry_numero_famille = tk.Entry(frame_ajouter)
    entry_numero_famille.grid(row=1, column=1)

    tk.Label(frame_ajouter, text="Date rentrer en stock:").grid(row=2, column=0)
    entry_date_rentrer = tk.Entry(frame_ajouter)
    entry_date_rentrer.grid(row=2, column=1)

    tk.Label(frame_ajouter, text="Designation:").grid(row=3, column=0)
    entry_designation = tk.Entry(frame_ajouter)
    entry_designation.grid(row=3, column=1)

    tk.Label(frame_ajouter, text="Refference :").grid(row=4, column=0)
    entry_refference = tk.Entry(frame_ajouter)
    entry_refference.grid(row=4, column=1)

    tk.Label(frame_ajouter, text="Prix :").grid(row=5, column=0)
    entry_prix = tk.Entry(frame_ajouter)
    entry_prix.grid(row=5, column=1)

    tk.Label(frame_ajouter, text="Quantite rentrer  :").grid(row=6, column=0)
    entry_quantite = tk.Entry(frame_ajouter)
    entry_quantite.grid(row=6, column=1)

    

    btn_ajouter = tk.Button(frame_ajouter, text="Ajouter", command=ajouter)
    btn_ajouter.grid(row=7, columnspan=2, pady=10)

    # Affichage des données
    frame_afficher = tk.Frame(root)
    frame_afficher.pack(pady=10)

    btn_afficher = tk.Button(frame_afficher, text="Afficher", command=afficher)
    btn_afficher.pack(pady=10)

    cols = ('Numéro produit', 'Numéro Famille','designation' ,'prix','quantite en stock','refferance','quantite stocker','date_entrer')
    tree = ttk.Treeview(frame_afficher, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)
    tree.pack()

    # Suppression de commande
    frame_supprimer = tk.Frame(root)
    frame_supprimer.pack(pady=10)

    tk.Label(frame_supprimer, text="Numéro de Commande à Supprimer:").grid(row=0, column=0)
    entry_numero_commande_supp = tk.Entry(frame_supprimer)
    entry_numero_commande_supp.grid(row=0, column=1)

    # Déconnexion
    btn_deconnecter = tk.Button(root, text="Menu Principal")
    btn_deconnecter.pack(pady=10)

    # Navigation
    frame_navigation = tk.Frame(root)
    frame_navigation.pack(pady=10)

    btn_bon_livraison = tk.Button(frame_navigation, text="Bon de Livraison")
    btn_bon_livraison.grid(row=0, column=0, padx=5)

    btn_facture = tk.Button(frame_navigation, text="Facture")
    btn_facture.grid(row=0, column=1, padx=5)

    root.mainloop()

def ajouter():
    numero_produit= entry_numero_produit.get()
    famille= entry_numero_famille.get()
    date= entry_date_rentrer.get()
    designation= entry_designation.get()
    quantite= entry_quantite.get()
    refference= entry_refference.get()
    prix= entry_prix.get()
   
    if not numero_produit or not famille or not prix or not date:
        messagebox.showerror("Erreur", "Tous ces champs sont obligatoires")
        return

    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        messagebox.showerror("Erreur", "Le format de la date est incorrect. Utilisez le format YYYY-MM-DD HH:MM:SS")
        return

    table = "produit"
    columns = ["NUMERO_PRODUIT", "NUMEROFAMILLE ", "DESIGNATION ","PRIX_PRODUIT","QUANTITE_STOCKER "," REFFERANCE"," DATE_ENTRER_"]
    values = (numero_produit,famille,designation,prix,quantite,refference,date)
    pass


def afficher():
    try:
        # Vider le treeview
        for row in tree.get_children():
            tree.delete(row)
        
        # Nom de la table
        table = "produit"
        print(f"Table: {table}")
        
        # Récupérer les données
        records=""
        #connexion a la database

        # Afficher les records pour le débogage
        print("Records après appel à afficher_donnees:", records)
        
        if records is not None and len(records) > 0:
            print("Insertion des données dans le treeview")
            for row in records:
                print("Row:", row)  # Afficher chaque ligne pour vérifier les données
                tree.insert("", tk.END, values=row)
        else:
            print("Aucun résultat trouvé ou records est None")
    
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")




if __name__ == "__main__":
    menu_produit()


#