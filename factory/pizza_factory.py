
class Pizza:
    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients
    
    def print(self):
        print(f'Ingredients of {self.name} are: {self.ingredients}')


class PizzaFactory:
    def createMargherita(self):
        name = 'Margherita'
        ingredients = ['Bread', 'Sauce', 'Cheese']
        return Pizza(name, ingredients)

    def createFarmhouse(self):
        name = 'Farmhouse'
        ingredients = ['Bread', 'Sauce', 'Cheese', 'Capsicum', 'Tomato']
        return Pizza(name, ingredients)
    
    def createPeppyPaneer(self):
        name = 'PeppyPaneer'
        ingredients = ['Bread', 'Sauce', 'Paneer']
        return Pizza(name, ingredients)


def main():
    pizza_factory = PizzaFactory()
    
    pizza_factory.createMargherita().print()
    pizza_factory.createFarmhouse().print()
    pizza_factory.createPeppyPaneer().print()
    

if __name__ == '__main__':
    main()