import threading
import os

lock = threading.Lock()

RESERVATION_FILE = "reservations.txt"

# Création du fichier s'il n'existe pas
if not os.path.exists(RESERVATION_FILE):
    open(RESERVATION_FILE, 'w').close()

class SalleReservation:
    def __init__(self):
        self.reservations = []

    def reserver_salle(self, salle, professeur, date, heure_debut, heure_fin):
        with lock:
            with open(RESERVATION_FILE, "a") as f:
                f.write(f"{salle}|{professeur}|{date}|{heure_debut}|{heure_fin}\n")
            print(f"Salle {salle} réservée avec succès pour {professeur} le {date} de {heure_debut} à {heure_fin}")

# Exemple d'utilisation
if __name__ == "__main__":
    reservation_system = SalleReservation()
    reservation_system.reserver_salle("Salle 101", "M. Keita", "2025-01-10", "10:00", "12:00")
