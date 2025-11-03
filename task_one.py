class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste is None:
            return "You have simple soda"
        else:
            return f"You have soda with {self.taste} taste"


soda_one = Soda(taste="Strawberry")
print(soda_one)

soda_two = Soda()
print(soda_two)