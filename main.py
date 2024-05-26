#! /usr/bin/python3
import mysql.connector
from mysql.connector import errors
import functions

conn = functions.initialisation()

print("*************************GESTIONNAIRE DE CONTACT***************************")
print("\t\t\t\tMENU : \n 1. Ajouter un nouveau contact\n 2. Supprimer un contact\n 3.Mettre à jour un contact\n 4. Afficher tous les contact\n 5. Rechercher un contact\n")
try :
    choix = int(input("Entrez une option : "))
    
except ValueError as VE :
    print("Vous devez entrer un nombre valide .\n\t\t", VE)

match choix :
    case 1 :
        #Ajouter un contact
        print("Fonction en cours !\n")
        functions.ajouter_contact(conn)
    case 2 :
        #Supprimer un contact
        print("Fonction en cours !\n")
        functions.supprimer_contact(conn)
    case 3 :
        #Mettre à jour un contact
        print("Fonction en cours !\n")
        functions.modifier_contact(conn)
    case 4 :
        #Afficher tous les contact
        print("Fonction en cours !\n")
        functions.afficher_contacts(conn)
    case 5 :
        #Rechercher un contact
        print("Fonction en cours !\n")
        id = int(input("Entrer l'ID : "))
        row = functions.rechercher_contact(conn, id)
        if row:
            print("ID   Nom         Prenom      Numéro de phone         Email")
            print("{}   {}      {}      {}      {}".format(row[0], row[1], row[2], row[3], row[4]))

        else:
            print("ID non trouvé !\n")

conn.close()



