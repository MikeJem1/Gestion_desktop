import sqlite3
from sqlite3 import Error

class MaBaseDeDonnees:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connexion = None
        self.curseur = None 

    def connecter(self):
        # Connexion à la base de données SQLite
        try:
            self.connexion = sqlite3.connect(self.db_file)
            self.curseur = self.connexion.cursor()
            print("Connexion réussie à la base de données SQLite")
        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connexion = None

    def deconnecter(self):
        # Déconnexion de la base de données
        if self.connexion:
            self.curseur.close()
            self.connexion.close()
            print("Déconnexion de la base de données.")
        else:
            print("Aucune connexion active à la base de données.")
    
    def supprimer_donnees(self, table, condition):
        # Méthode pour supprimer des données
        try:
            requete = f"DELETE FROM {table} WHERE {condition}"
            self.curseur.execute(requete)
            self.connexion.commit()
            print("Données supprimées avec succès.")
        except Error as e:
            print(f"Erreur lors de la suppression des données : {e}")

    def afficher_donnees(self, table):
        # Méthode pour afficher des données
        try:
            requete = f"SELECT * FROM {table}"
            self.curseur.execute(requete)
            records = self.curseur.fetchall()
            
            records = list(records) # Convertir en liste
            print(f"Records convertis en liste : {records}")

            for row in records:
                print(row)

            return records if records else [] # Retourner les enregistrements
        except Error as e:
            print(f"Erreur lors de l'affichage des données : {e}")
            return []
        
    def afficher_donnees_disct(self, table, condition):
        try:
            requete = f"SELECT * FROM {table} WHERE {condition}"
            self.curseur.execute(requete)
            records = self.curseur.fetchall()
            
            records = list(records) # Convertir en liste
            print(f"Records convertis en liste : {records}")

            for row in records:
                print(row)

            return records if records else [] # Retourner les enregistrements
        except Error as e:
            print(f"Erreur lors de l'affichage des données : {e}")
            return []   
        
    def executer_requete(self, table, columns, valeurs=None):
        # Exécution d'une requête simple
        if self.connexion is None:
            self.connecter()
        try:
            # Concaténation des noms de colonnes et des valeurs avec des virgules
            columns_str = ', '.join(columns)
            values_str = ', '.join(['?'] * len(columns))  # ? pour chaque valeur à insérer

            # Construction de la requête SQL
            request = f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})"

            print(f"Executing SQL: {request}")
            print(f"With values: {valeurs}")

            self.curseur.execute(request, valeurs)
            self.connexion.commit()
        except Error as e:
            print(f"Erreur lors de l'enregistrement : {e}")
            

    def executer_requete_joint(self, requete):
        # Exécution d'une requête avec jointure
        if self.connexion is None:
            self.connecter()
        try:
            self.curseur.execute(requete)
            records = self.curseur.fetchall()
            records = list(records) # Convertir en liste
            print(f"Records convertis en liste : {records}")

            for row in records:
                print(row)

            return records if records else [] # Retourner les enregistrements
        except Error as e:
            print(f"Erreur lors de l'affichage des données : {e}")
            return []
        
    def executer_requete_2(self, query, params=None):
        try:
            if params:
                self.curseur.execute(query, params)
            else:
                self.curseur.execute(query)
            self.connexion.commit()
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête: {e}")
            self.connexion.rollback()
        

    def executer_requete_joint_2(self, query, params=None):
        try:
            if params:
                self.curseur.execute(query, params)
            else:
                self.curseur.execute(query)
            return self.curseur.fetchall()
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête jointe: {e}")
            return []
        
# Exemple d'utilisation
db = MaBaseDeDonnees('database.db')
db.connecter()
