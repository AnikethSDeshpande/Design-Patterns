'''
    Zoo is a place where we can add animals of different kinds.
    
    Animals can introduce themselves regarding how they move and
    how they communicate to the visitors.
'''


class Animal:
    def __init__(self, species: str, name: str, features: dict):
        self.species = species
        self.name = name
        self.features = {}

        for key, value in features.items():
            self.features[key] = value
    
    def introduce(self):
        introduction = f'''
                            Hi there, I am a {self.species} and my name is {self.name}.
                            I {self.features.get('locomotory_movement')} to find food.
                            I {self.features.get('communicate')} to communicate.
                        '''
        
        print(introduction)


class AnimalFactory:
    def createCowFactory(self):
        species = 'Cow'
        name = 'Stacey'
        features = {
            'locomotory_movement': 'walk',
            'communicate': 'meow'
        }

        return Animal(species, name, features)
    
    def createEagleFactory(self):
        species = 'Eagle'
        name = 'Joe'
        features = {
            'locomotory_movement': 'fly',
            'communicate': 'screech'
        }

        return Animal(species, name, features)
    
    def createDolphineFactory(self):
        species = 'Ben'
        name = 'Joe'
        features = {
            'locomotory_movement': 'swim',
            'communicate': 'whistle and click'
        }

        return Animal(species, name, features)


def main():
    animal_factory = AnimalFactory()
    
    animal_factory.createCowFactory().introduce()
    animal_factory.createEagleFactory().introduce()
    animal_factory.createDolphineFactory().introduce()
    


if __name__ == '__main__':
    main()