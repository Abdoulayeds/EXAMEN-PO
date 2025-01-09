from banque.banque import creer_compte  # Importer les fonctions de la banque
from reservation.reservation import SalleReservation  # Importer les fonctions de réservation
import threading

def afficher_menu_principal():
    """
    Affiche le menu principal et permet à l'utilisateur de choisir un service.
    """
    print("Bienvenue sur le Serveur Magique !")
    print("1. Services bancaires")
    print("2. Réservation de salle de TP")
    print("3. Quitter")

    choix = input("Veuillez entrer le numéro de votre choix : ")

    if choix == "1":
        menu_banque()
    elif choix == "2":
        menu_reservation()
    elif choix == "3":
        print("Merci d'avoir utilisé le Serveur Magique. À bientôt !")
        exit()
    else:
        print("Choix invalide. Veuillez réessayer.")
        afficher_menu_principal()

def menu_banque():
    """
    Menu pour les services bancaires.
    """
    print("\n--- Services Bancaires ---")
    print("1. Créer un compte")
    print("2. Consulter un compte")
    print("3. Faire un dépôt")
    print("4. Faire un retrait")
    print("5. Faire un virement")
    print("6. Modifier le code PIN")
    print("7. Fermer un compte")
    print("8. Retour au menu principal")

    choix = input("Veuillez entrer le numéro de votre choix : ")

    if choix == "1":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        numero_telephone = input("Numéro de téléphone : ")
        type_compte = input("Type de compte (courant/epargne) : ")
        pin = input("Code PIN (4 chiffres) : ")
        creer_compte(nom, prenom, numero_telephone, type_compte, pin)
    elif choix == "8":
        afficher_menu_principal()
    else:
        print("Fonctionnalité non encore implémentée.")
        menu_banque()

def menu_reservation():
    """
    Menu pour la réservation des salles de TP.
    """
    reservation_system = SalleReservation()

    print("\n--- Système de Réservation de Salles ---")
    print("1. Réserver une salle")
    print("2. Retour au menu principal")

    choix = input("Veuillez entrer le numéro de votre choix : ")

    if choix == "1":
        salle = input("Nom ou numéro de la salle : ")
        professeur = input("Nom du professeur : ")
        date = input("Date de réservation (YYYY-MM-DD) : ")
        heure_debut = input("Heure de début (HH:MM) : ")
        heure_fin = input("Heure de fin (HH:MM) : ")
        reservation_system.reserver_salle(salle, professeur, date, heure_debut, heure_fin)
    elif choix == "2":
        afficher_menu_principal()
    else:
        print("Choix invalide. Veuillez réessayer.")
        menu_reservation()

# Point d'entrée principal
if __name__ == "__main__":
    afficher_menu_principal()
