#coding utf-8

import mysql.connector
from mysql.connector import Error

def initialisation():
    '''Elle initialise la connexion que va utiliser le long du programme pour
    intéragir avec la base de données'''
    try :
        connexion = mysql.connector.connect(
        host = 'localhost',
        user = 'user1',
        password = '123456789',
        database = 'project'
        )
        checker = connexion.is_connected()
        if checker:
            print("*******************************Connexion à la Base de données réussie !**************************\n")
        
    except ConnectionError as e:
        print("\t\t\tConnexion à la base de données échouée !\n\t\t\t", e)
    
    if checker:
        cursor = connexion.cursor()
        #cursor.execute('''CREATE DATABASE projet IF NOT EXISTS''')
        #conn.commit()
        #cursor.execute('''USE DATABASE contact''')
        #conn.commit()
        cursor.execute(
        ''' CREATE TABLE IF NOT EXISTS contact(
            id INT primary key auto_increment,
            nom VARCHAR(50) NOT null,
            prenom VARCHAR(50) NOT null,
            numero_phone INT not null,
            email VARCHAR(50)
            )'''
        )
        return connexion


def ajouter_contact(connexion): #La fonction reçoit un curseur de connexion à la base de donnée
    
    last_name = input("Nom : ")
    first_name = input("Prénom : ")
    try :
        cell_number = int(input("Numéro de téléphone : "))
    except ValueError as e:
        print("Le Numéro de téléphone doit être un entier !\n\t\t\t", e)
    
    email = input("Adresse mail : ")

    #Enregistrement dans la database
    #connexion = mysql.connector.connect()
    cursor = connexion.cursor()
    cursor.execute('''INSERT INTO contact (nom, prenom, numero_phone, email) 
                   VALUES ('{}', '{}', '{}', '{}')'''.format(last_name, first_name, cell_number, email)
                )
    connexion.commit() #On envoie l'ajout à la database
    print("\t\t\tENREGISTREMENT REUSSI !\n")


def supprimer_contact(connexion): #La fonction reçoit un curseur de connexion à la base de donnée
    
    try :
        id = int(input("Entrer l'ID : "))
    except ValueError as e:
        print("\t\t\t Erreur, vous devez entrer un nombre.\n\t\t\t", e)

    #connexion = mysql.connector.connect()
    row = rechercher_contact(connexion, id)
    if row:
        cursor = connexion.cursor()
        cursor.execute(
            '''DELETE FROM contact WHERE id = {}'''.format(id)
        )
        connexion.commit()


def modifier_contact(connexion):#Elle reçoit en paramètre une connexion à la base de donnée
    id  = input("Entrer l'ID : ")
    row = rechercher_contact(connexion, id)
    if row :
        tel = input("Entrer le nouveau numéro : ")
        cursor = connexion.cursor()
        cursor.execute(
            '''UPDATE contact SET numero_phone = {} WHERE id = {}'''.format(tel, id)
        )
        connexion.commit()

    else :
        print("L'ID n'existe pas !\n")


def afficher_contacts(connexion):
    #connexion = mysql.connector.connect()
    cursor = connexion.cursor()
    cursor.execute(
        '''SELECT * FROM contact'''
    )

    print("ID   Nom         Prenom      Numéro de phone         Email")
    rows = cursor.fetchall()
    for row in rows:
        print("{}   {}      {}      {}      {}".format(row[0], row[1], row[2], row[3], row[4]))

def rechercher_contact(connexion, id):
    #id = input("Entrer l'ID du contact : ")
    #connexion = mysql.connector.connect()
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM contact WHERE id = {}".format(id))
    row = cursor.fetchone()
    return row

def fermeture(connexion):#Elle reçoit en paramètre la connexion à fermer
    #connexion = mysql.connector.connect()
    #cursor = connexion.cursor()
    connexion.close()

'''#Création d'un curseur
cursor = conn.cursor()

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()'''