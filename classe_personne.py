# Little scale school's management application

# By: Someone Else

# Class to "create" people
class Personne:
    # The Constructor:
    def __init__(self, nom:str, age):
        self.the_name = nom
        self.the_age = age


    # Print person's info method
    def afficher_infos(self):
        """This function displays info about the person

        Args:
            nom(str)
            age(int)
        Returns:
            (str)

        """

        name_cleaned = self.the_name.strip().capitalize()

        return f"Name: {name_cleaned}\nAge: {self.the_age}"


