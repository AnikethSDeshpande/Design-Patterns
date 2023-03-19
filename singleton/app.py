'''
    Singleton design pattern is used to ensure only one instance of class is created.
'''


class App:
    __instance = None

    @staticmethod
    def get_instance():
        if not App.__instance:
            App.__instance = App('Default', 'This is the default app created.')
        return App.__instance
    
    def __init__(self, name = 'Default', description = None) -> None:
        if not App.__instance:
            self.app_name = name
            self.description = description
            App.__instance = self
        else:
            raise Exception('Singleton cannot be instantiated more than once')
    
    def __str__(self) -> str:
        return f'''
            App name: {self.app_name}
            Description: {self.description}
        '''

a1 = App('AuraApp', 'App for managing Aura 23')
print(a1)

a2 = App.get_instance()
a2.app_name = 'AURA APP'
a2.description = 'App for managing AURA 23'
print(a2)

print('a1 is a2: ', a1 is a2)
