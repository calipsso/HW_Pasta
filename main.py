class Supplements:
    def __init__(self):
        self.ingredients = []
    def add_ingredient(self, item):
        self.ingredients.append(item)

    def __str__(self):
        return " and ".join(self.ingredients)

class Pasta:
    def __init__(self):
        self.supplement = Supplements()
    def add_pomodoro(self):
        self.supplement.add_ingredient("Pomodoro")
        return self
    def add_garlic(self):
        self.supplement.add_ingredient("Garlick")
        return self
    def add_olio(self):
        self.supplement.add_ingredient("Olive oil")
        return self
    def builder(self):
        recept = self.supplement
        self.supplement = Supplements()
        return recept

pasta = Pasta()

recipe = pasta.add_pomodoro().add_garlic().add_olio().builder()
recipe1 = pasta.add_pomodoro().builder()
recipe2 = pasta.add_garlic().add_olio().builder()

print(f"Pasta with {recipe}")
print(f"Pasta with {recipe1}")
print(f"Pasta with {recipe2}")





