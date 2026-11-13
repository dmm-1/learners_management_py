# --------    ----------  ----------  -------------

# Importing necessary classes
from classe_personne import Personne        # classe_personne.py is the module
from functools import reduce

# Class to "create" students (inherits from Personne)
class Etudiant(Personne):
    # The constructor
    def __init__(self, nom, age, filiere, matricule, notes:list = None):
        super().__init__(nom, age)
        self.student_id = matricule
        self.student_field = filiere

        # Checking notes[] status before creating the list
            # 1. if there's no grades when "creating" the student
        if (notes is None):
            notes = []                   # we create an empty liste 
            self.student_grades = notes

            #2. if the student already have marks while "creating him"
        else:
                            # we directly use these given marks to create the list
            self.student_grades = notes  

        # We can also write these conditions as:
        # self.student_grades = [] if notes is None else notes,
        # meaning student grades is an empty list if there's no marks given
        # at the intanciation. Else, meaning there's already one or more marks,
        # use them directly in the new list.



    # Method to add grades in "notes":
    def ajouter_note(self, note_to_add:float):
        """This function add a new mark

        Args:
            note_to_add(float)
        Returns:
            nothing
        """
        
        if ((0 <= note_to_add) and (note_to_add <= 20)):
            self.student_grades.append(note_to_add)

        else:
            raise ValueError("Note invalide. Veuillez respecter [0 <= votre_note <= 20]")


    # Method to calculate the average grade:
    def calculer_moyenne(self):
        """This function calculates the average mark

        Args:
            student_grades(list, attribute of the Class)
        Returns:
            - 0 if there's no mark in student_grades
            - the calculated average_mark(float) else
        """
        # if there's no mark
        if not self.student_grades:
            return 0

        # if there's one or more mark:
        else:
            average_grade = float((sum(self.student_grades)) / len(self.student_grades))

            # reduce(self.student_grades, lambda grades_sum, grades_size)

            return average_grade





# Test du code:
student1 = Etudiant("Awa", 20, "BTS", "M001")
student2 = Etudiant("Moussa", 21, "Licence 2", "M029", [10, 18.5, 7.25])

print(f"Les notes de {student1.the_name} sont: {student1.student_grades}")
print(f"Les notes de {student2.the_name} sont: {student2.student_grades}")

student1.ajouter_note(17.75)
student2.ajouter_note(14)

print("Après ajout d\'une nouvelle note pour chacun: ")

print(f"\t- les notes de {student1.the_name} sont: {student1.student_grades}")
print(f"\t- les notes de {student2.the_name} sont: {student2.student_grades}")

print(f"Calcul des moyennes de {student1.the_name} et {student2.the_name} :")
print(f"\t- la moyenne de  {student1.the_name} est : [{student1.calculer_moyenne()}]")
print(f"\t- la moyenne de  {student2.the_name} est : [{student2.calculer_moyenne()}]")