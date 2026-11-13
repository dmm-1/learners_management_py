
# ---------------   ---------------    ---------------     ---------------

# Importing necessary package
from classe_etudiant import Etudiant


# Class to manage students

class GestionEtudiants:
    def __init__(self):
        self.liste_etudiants = []
        self.id_counter = 1

    # Method to add students:
    def ajouter_etudiant(self, name:str, field:str, age:int, notes:list = None):
        """This method create a new Etudiant object, and add it to the liste_etudiants list

        Args:
            name(str)
            fiel(str)
            age(int)
            notes(list)

        Returns:
            (Etudiant)
        """

        self.liste_etudiants.append(Etudiant(name, age, field, matricule=self.id_counter, notes=notes))
        self.id_counter += 1        