class Restaurant():
    """A simple restaurant class."""
    def __init__(self,res_name, cuis_type):
        """Initialize name and cuisine type."""
        self.name = res_name
        self.type = cuis_type
    def describe_restaurant(self):
        print("This restaurant's name is: " + self.name.title() + '.')
        print(self.name.title() + " serves " + self.type.title() + ".")
    def open_res(self):
        print("Now "+ self.name + " is open!")
"""res1 = Restaurant("chi's", "chinese cuisine")
res1.describe_restaurant()
res2 = Restaurant("Pho", "thai cuisine")
res2.describe_restaurant()
res3 = Restaurant("Mcdonald", "fast food")
res3.describe_restaurant()
"""
class User():
    def __init__(self, f_name, l_name, sex, age):
        self.first_name = f_name
        self.last_name = l_name
        self.sex = sex
        self.age = age
    def describe_user(self):
        print("This user's name is: " + self.first_name + " " + self.last_name)
        #print ("this is a number: %d." % (8))
        print("Sex is: %s and age %d." % (self.sex, self.age))
    def greet_user(self):
        print("Have a good day! " + self.first_name + ' ' + self.last_name)
u1 = User("Rubing", "Guo", "F", 15)
u1.describe_user()

u2 = User("Taylor", "Swift", "F", 28)
u2.describe_user()
