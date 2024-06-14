import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Requêtes pour supprimer les tables si elles existent
tables = [
    "APPARTENIR", "CLIENT", "COLIS", "COMMANDE", "DEPARTEMENT", 
    "EMPLOYER", "FACTURE", "FAMILLE_DE_PRODUIT", "LIVRAISON", 
    "PRODUIT", "REGLEMENT"
]
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Requêtes de création des tables avec contraintes de clé étrangère
create_table_queries = [
    """
    CREATE TABLE APPARTENIR (
        NUMERO_COMMANDE INTEGER NOT NULL,
        NUMERO_PRODUIT INTEGER NOT NULL,
        NUMERO_LIGNE INTEGER,
        QUANTITE_PROD INTEGER,
        QUANTTE_LIVRER INTEGER,
        QUANTITE_COMMANDER INTEGER,
        PRIMARY KEY (NUMERO_COMMANDE, NUMERO_PRODUIT),
        FOREIGN KEY (NUMERO_COMMANDE) REFERENCES COMMANDE (NUMERO_COMMANDE) ON DELETE RESTRICT ON UPDATE RESTRICT,
        FOREIGN KEY (NUMERO_PRODUIT) REFERENCES PRODUIT (NUMERO_PRODUIT) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """,
    """
    CREATE TABLE CLIENT (
        NUMERO_CLI INTEGER NOT NULL,
        RAISONSOCIAL TEXT,
        ADRESSECLI TEXT,
        TELEPHONECLI TEXT,
        TOTALFACTURE INTEGER,
        TOTALREGLEMENT INTEGER,
        PRIMARY KEY (NUMERO_CLI)
    )
    """,
    """
    CREATE TABLE COLIS (
        NUMERO_COLIS INTEGER NOT NULL,
        CODE_EMP INTEGER NOT NULL,
        NUMERO_LIVRAISON INTEGER NOT NULL,
        NUMERO_COMMANDE INTEGER NOT NULL,
        DATE_EXPEDITION DATE,
        STATUS_COLIS BLOB,
        ADRESSE_DE_LIV TEXT,
        PRIMARY KEY (NUMERO_COLIS),
        FOREIGN KEY (CODE_EMP) REFERENCES EMPLOYER (CODE_EMP) ON DELETE RESTRICT ON UPDATE RESTRICT,
        FOREIGN KEY (NUMERO_COMMANDE) REFERENCES COMMANDE (NUMERO_COMMANDE) ON DELETE RESTRICT ON UPDATE RESTRICT,
        FOREIGN KEY (NUMERO_LIVRAISON) REFERENCES LIVRAISON (NUMERO_LIVRAISON) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """,
    """
    CREATE TABLE COMMANDE (
        NUMERO_COMMANDE INTEGER NOT NULL,
        NUMERO_CLI INTEGER NOT NULL,
        DATE_COMMANDE TIMESTAMP NOT NULL,
        INDICE_LIVRAISON BOOLEAN,
        PRIMARY KEY (NUMERO_COMMANDE),
        FOREIGN KEY (NUMERO_CLI) REFERENCES CLIENT (NUMERO_CLI) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """,
    """
    CREATE TABLE DEPARTEMENT (
        CODE_DEPT TEXT NOT NULL,
        NOM_DEPT TEXT,
        PRIMARY KEY (CODE_DEPT)
    )
    """,
    """
    CREATE TABLE EMPLOYER (
        CODE_EMP INTEGER NOT NULL,
        CODE_DEPT TEXT NOT NULL,
        NOMEMP TEXT,
        PRENOMEMP TEXT,
        DATE_DE_NAISSANCE DATE,
        ADRESSEEMP TEXT,
        DATE_EMBAUCHE DATE,
        PRIMARY KEY (CODE_EMP),
        FOREIGN KEY (CODE_DEPT) REFERENCES DEPARTEMENT (CODE_DEPT) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """,
    """
    CREATE TABLE FACTURE (
        NUMEROFACTURE INTEGER NOT NULL,
        NUMERO_CLI INTEGER NOT NULL,
        DATEFAC TIMESTAMP,
        MONTANT_FAC DECIMAL,
        TAUXTVA DECIMAL,
        MONTANTTVA DECIMAL,
        PRIMARY KEY (NUMEROFACTURE),
        FOREIGN KEY (NUMERO_CLI) REFERENCES CLIENT (NUMERO_CLI) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """,
    """
    CREATE TABLE FAMILLE_DE_PRODUIT (
        NUMEROFAMILLE INTEGER NOT NULL,
        LIBELE INTEGER,
        PRIMARY KEY (NUMEROFAMILLE)
    )
    """,
    """
    CREATE TABLE LIVRAISON (
        NUMERO_LIVRAISON INTEGER NOT NULL,
        DATE_ENTRER_ TIMESTAMP,
        NOMBRE_DE_COLIS INTEGER,
        POIDS_COLI DECIMAL,
        FRAIS_COLIS DECIMAL,
        TRANSPORTEUR TEXT,
        PRIMARY KEY (NUMERO_LIVRAISON)
    )
    """,
    """
    CREATE TABLE PRODUIT (
        NUMERO_PRODUIT INTEGER NOT NULL,
        NUMEROFAMILLE INTEGER NOT NULL,
        DESIGNATION TEXT,
        PRIX_PRODUIT FLOAT,
        QUANTITE_STOCK INTEGER,
        REFFERANCE TEXT NOT NULL,
        QUANTITE_STOCKER INTEGER,
        DATE_ENTRER_ TIMESTAMP,
        PRIMARY KEY (NUMERO_PRODUIT),
        FOREIGN KEY (NUMEROFAMILLE) REFERENCES FAMILLE_DE_PRODUIT (NUMEROFAMILLE) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """,
    """
    CREATE TABLE REGLEMENT (
        NUMERO_REG INTEGER NOT NULL,
        NUMEROFACTURE INTEGER NOT NULL,
        DATE_REGLEMENT TIMESTAMP,
        TYPE_REGLEMENT TEXT,
        LIBELLE_RE TEXT,
        MONTANT DECIMAL,
        DATE_ECHEANT DATE,
        PRIMARY KEY (NUMERO_REG),
        FOREIGN KEY (NUMEROFACTURE) REFERENCES FACTURE (NUMEROFACTURE) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
    """
]

# Exécution des requêtes de création des tables
for query in create_table_queries:
    cursor.execute(query)

# Validation des changements
conn.commit()

# Fermeture de la connexion
conn.close()