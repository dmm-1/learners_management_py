# ---------------   ---------------    ---------------     ---------------

# Importing necessary package
from classe_etudiant import Etudiant


# Class to manage students
    # We respect 'Factory', 'Orchestrator', architecture here.
    # Domain Driven Design.

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


    # Method to list all Students of the School (with their infos):
    def afficher_etudiants(self):
        """This method displays all Students with their data
        Args:
            None
        Returns:
            list of the Students(str)
        """

        for students in self.liste_etudiants:
            print(f"{students.student_id}\t {students.the_name}\t {students.the_age}\t{students.student_field}",)

        print("Pour voir les notes d\'un étudiant, sélectionnez [Rechercher un étudiant], et renseignez son matricule")


# Tests bloc

# Creating new school:

Limamoulaye = GestionEtudiants()

# Adding a new Student into this school
Limamoulaye.ajouter_etudiant("Jean Duverne", "Maintenance des Infrastures Critiques", 22, [15, 18.5, 17, 19])
Limamoulaye.ajouter_etudiant("Patrick Germaint", "Analyses Financières", 26, [12, 16.65])

# Displaying all Students of this School:
Limamoulaye.afficher_etudiants()