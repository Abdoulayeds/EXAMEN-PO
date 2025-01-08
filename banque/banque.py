import threading
import os

lock = threading.Lock()

# Fichiers nécessaires
CLIENT_FILE = "client.txt"
TRANSACTION_FILE = "transaction.txt"

# Création des fichiers s'ils n'existent pas
if not os.path.exists(CLIENT_FILE):
    open(CLIENT_FILE, 'w').close()

if not os.path.exists(TRANSACTION_FILE):
    open(TRANSACTION_FILE, 'w').close()

def creer_compte(nom, prenom, numero_telephone, type_compte, pin):
    with lock:
        num_compte = str(hash(numero_telephone))[:8]  # Génère un identifiant unique
        solde = 5000 if type_compte == "epargne" else 0
        statut = "Actif"
        with open(CLIENT_FILE, "a") as f:
            f.write(f"{num_compte}|{nom}|{prenom}|{numero_telephone}|{type_compte}|{solde}|{pin}|{statut}\n")
        print(f"Compte créé avec succès ! Numéro de compte : {num_compte}")
        return num_compte

# Exemple d'utilisation
if __name__ == "__main__":
    creer_compte("Doe", "John", "1234567890", "epargne", "1234")
